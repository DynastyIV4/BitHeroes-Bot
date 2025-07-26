from core.controllers.ConfigurationControllerModel import ConfigurationControllerModel
from core.StateMachine import StateMachine
from core.Logger import Logger
from gui.views.OnOffButtonView import OnOffButtonView
from core.GameInterface import GameInterface

from threading import Thread
import time

class AutoPilotStarter:
    def __init__(self, 
                 game_automation_controllers: list[ConfigurationControllerModel], 
                 settings_configuration_controllers: list[ConfigurationControllerModel],
                 button: OnOffButtonView,
                 state_machine: StateMachine, 
                 game_interface: GameInterface,
                 logger: Logger):
        self.game_automation_controllers = game_automation_controllers
        self.settings_configuration_controllers = settings_configuration_controllers
        self.controllers = game_automation_controllers + settings_configuration_controllers
        self.state_machine = state_machine
        self.game_interface = game_interface
        self.logger = logger
        self.button = button
        self.process_thread = Thread(target=self.autopilot_loop, daemon=True)

        self.button.set_callback(self.on_button_on_off_pressed)


    def on_button_on_off_pressed(self):
        self.start() if not self.button.is_pressed else self.stop()

    def start(self):
        is_ready_to_start = True
        at_least_one_automation_selected = False

        for controller in self.controllers:
            is_ready_to_start &= controller.is_configuration_ready()
        
        if not is_ready_to_start:
            self.logger.print("Autopilot is not ready to start. Please check your configurations.")
            return
        
        for controller in self.game_automation_controllers:
            if controller.is_enabled():
                at_least_one_automation_selected |= True

        if not at_least_one_automation_selected:
            self.logger.print("You must enable at least one automation to start the autopilot.")
            return
        
        if self.game_interface.is_game_running() and not self.game_interface.is_home_state():
            self.logger.print("You must be on the home screen to start the autopilot and make sure no window is open.")
            return
        
        self.button.press()

        for controller in self.controllers:
            controller.disable_view()
        
        self.logger.print("Starting the autopilot with the configured settings...")
        if not self.process_thread.is_alive():
            self.process_thread.start()
        else:
            self.state_machine.is_stopped = False


    def stop(self):
        self.logger.print("Request to stop the autopilot received. Stopping...")
        self.state_machine.stop()

    def autopilot_loop(self):
        while True:
            self.state_machine.is_stop_checking_enabled = False
            while self.state_machine.is_stopped:
                time.sleep(0.1)
            self.state_machine.is_stop_checking_enabled = True
            self.state_machine.automation_machine.reset_ressources()
            self.logger.print("=== Autopilot is RUNNING 🟢===")
            self.state_machine.run()
            self.logger.print("=== Autopilot has stopped 🛑 ===")
            self.button.press()

            for controller in self.controllers:
                controller.restore_view()
            self.logger.print("You can now change settings or exit the application.")



