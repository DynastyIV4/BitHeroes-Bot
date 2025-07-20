import pytest 
from core.text_identifiers.FamiliarIdentifier import FamiliarIdentifier
from core.text_identifiers.WormIdentifier import WormIdentifier
from PIL import Image

def _test_identify_worm(image_path: str) -> int:
    image = Image.open(image_path)
    return WormIdentifier.identify(image)

# ------------------
# LEGENDARY WORM TESTS
# ------------------

def test_identify_26_legendary_worm():
    result: int = _test_identify_worm("tests/test_images/legendary_worm_1.png")
    assert result == 26, "Worm number recognition failed."

def test_identify_25_legendary_worm():
    result: int = _test_identify_worm("tests/test_images/legendary_worm_2.png")
    assert result == 25, "Worm number recognition failed."

def test_identify_24_legendary_worm():
    result: int = _test_identify_worm("tests/test_images/legendary_worm_3.png")
    assert result == 24, "Worm number recognition failed."

def test_identify_23_legendary_worm():
    result: int = _test_identify_worm("tests/test_images/legendary_worm_4.png")
    assert result == 23, "Worm number recognition failed."

def test_identify_22_legendary_worm():
    result: int = _test_identify_worm("tests/test_images/legendary_worm_5.png")
    assert result == 22, "Worm number recognition failed."

def test_identify_21_legendary_worm():
    result: int = _test_identify_worm("tests/test_images/legendary_worm_6.png")
    assert result == 21, "Worm number recognition failed."

def test_identify_20_legendary_worm():
    result: int = _test_identify_worm("tests/test_images/legendary_worm_7.png")
    assert result == 20, "Worm number recognition failed."

def test_identify_19_legendary_worm():
    result: int = _test_identify_worm("tests/test_images/legendary_worm_8.png")
    assert result == 19, "Worm number recognition failed."

def test_identify_18_legendary_worm():
    result: int = _test_identify_worm("tests/test_images/legendary_worm_9.png")
    assert result == 18, "Worm number recognition failed."

def test_identify_17_legendary_worm():
    result: int = _test_identify_worm("tests/test_images/legendary_worm_10.png")
    assert result == 17, "Worm number recognition failed."

# ------------------
# EPIC WORM TESTS
# ------------------

def test_identify_77_epic_worm():
    result: int = _test_identify_worm("tests/test_images/epic_worm_1.png")
    assert result == 77, "Worm number recognition failed."

def test_identify_76_epic_worm():
    result: int = _test_identify_worm("tests/test_images/epic_worm_2.png")
    assert result == 76, "Worm number recognition failed."

def test_identify_79_epic_worm():
    result: int = _test_identify_worm("tests/test_images/epic_worm_3.png")
    assert result == 79, "Worm number recognition failed."

def test_identify_78_epic_worm():
    result: int = _test_identify_worm("tests/test_images/epic_worm_4.png")
    assert result == 78, "Worm number recognition failed."

def test_identify_74_epic_worm():
    result: int = _test_identify_worm("tests/test_images/epic_worm_5.png")
    assert result == 74, "Worm number recognition failed."

def test_identify_73_epic_worm():
    result: int = _test_identify_worm("tests/test_images/epic_worm_6.png")
    assert result == 73, "Worm number recognition failed."

def test_identify_72_epic_worm():
    result: int = _test_identify_worm("tests/test_images/epic_worm_7.png")
    assert result == 72, "Worm number recognition failed."

def test_identify_75_epic_worm():
    result: int = _test_identify_worm("tests/test_images/epic_worm_8.png")
    assert result == 75, "Worm number recognition failed."

def test_identify_71_epic_worm():
    result: int = _test_identify_worm("tests/test_images/epic_worm_9.png")
    assert result == 71, "Worm number recognition failed."

def test_identify_70_epic_worm():
    result: int = _test_identify_worm("tests/test_images/epic_worm_10.png")
    assert result == 70, "Worm number recognition failed."

# ------------------
# RARE WORM TESTS
# ------------------

def test_identify_127_rare_worm():
    result: int = _test_identify_worm("tests/test_images/rare_worm_1.png")
    assert result == 127, "Worm number recognition failed."

def test_identify_125_rare_worm():
    result: int = _test_identify_worm("tests/test_images/rare_worm_2.png")
    assert result == 125, "Worm number recognition failed."

def test_identify_126_rare_worm():
    result: int = _test_identify_worm("tests/test_images/rare_worm_3.png")
    assert result == 126, "Worm number recognition failed."

def test_identify_124_rare_worm():
    result: int = _test_identify_worm("tests/test_images/rare_worm_4.png")
    assert result == 124, "Worm number recognition failed."

def test_identify_123_rare_worm():
    result: int = _test_identify_worm("tests/test_images/rare_worm_5.png")
    assert result == 123, "Worm number recognition failed."

def test_identify_122_rare_worm():
    result: int = _test_identify_worm("tests/test_images/rare_worm_6.png")
    assert result == 122, "Worm number recognition failed."

def test_identify_121_rare_worm():
    result: int = _test_identify_worm("tests/test_images/rare_worm_7.png")
    assert result == 121, "Worm number recognition failed."

def test_identify_120_rare_worm():
    result: int = _test_identify_worm("tests/test_images/rare_worm_8.png")
    assert result == 120, "Worm number recognition failed."

def test_identify_119_rare_worm():
    result: int = _test_identify_worm("tests/test_images/rare_worm_9.png")
    assert result == 119, "Worm number recognition failed."

def test_identify_118_rare_worm():
    result: int = _test_identify_worm("tests/test_images/rare_worm_10.png")
    assert result == 118, "Worm number recognition failed."

# ------------------
# COMMON WORM TESTS
# ------------------

def test_identify_169_common_worm():
    result: int = _test_identify_worm("tests/test_images/common_worm_1.png")
    assert result == 169, "Worm number recognition failed."

def test_identify_168_common_worm():
    result: int = _test_identify_worm("tests/test_images/common_worm_2.png")
    assert result == 168, "Worm number recognition failed."

def test_identify_167_common_worm():
    result: int = _test_identify_worm("tests/test_images/common_worm_3.png")
    assert result == 167, "Worm number recognition failed."

def test_identify_166_common_worm():
    result: int = _test_identify_worm("tests/test_images/common_worm_4.png")
    assert result == 166, "Worm number recognition failed."

def test_identify_165_common_worm():
    result: int = _test_identify_worm("tests/test_images/common_worm_5.png")
    assert result == 165, "Worm number recognition failed."

def test_identify_164_common_worm():
    result: int = _test_identify_worm("tests/test_images/common_worm_6.png")
    assert result == 164, "Worm number recognition failed."

def test_identify_159_common_worm():
    result: int = _test_identify_worm("tests/test_images/common_worm_7.png")
    assert result == 159, "Worm number recognition failed."

def test_identify_162_common_worm():
    result: int = _test_identify_worm("tests/test_images/common_worm_8.png")
    assert result == 162, "Worm number recognition failed."

def test_identify_161_common_worm():
    result: int = _test_identify_worm("tests/test_images/common_worm_9.png")
    assert result == 161, "Worm number recognition failed."

def test_identify_160_common_worm():
    result: int = _test_identify_worm("tests/test_images/common_worm_10.png")
    assert result == 160, "Worm number recognition failed."
