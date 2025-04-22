# server.py
from os import path

from mcp.server.fastmcp import FastMCP
import pyautogui

# Create an MCP server
mcp = FastMCP("pyautogui")


@mcp.tool()
def get_screen_size() -> tuple[int, int]:
    """Get the screen width and height."""
    return pyautogui.size()


@mcp.tool()
def get_mouse_position() -> tuple[int, int]:
    """Get the current mouse cursor position."""
    return pyautogui.position()


@mcp.tool()
def move_mouse_to(x: int, y: int) -> None:
    """Move the mouse to the specified x, y coordinates."""
    pyautogui.moveTo(x, y)


@mcp.tool()
def click_mouse(x: int = None, y: int = None) -> None:
    """Click the mouse at the specified x, y coordinates or current position."""
    pyautogui.click(x, y)


@mcp.tool()
def move_mouse_relative(x_offset: int = 0, y_offset: int = 0) -> None:
    """Move the mouse relative to its current position."""
    pyautogui.move(x_offset, y_offset)


@mcp.tool()
def double_click_mouse() -> None:
    """Double-click the mouse at its current position."""
    pyautogui.doubleClick()


@mcp.tool()
def move_mouse_with_tween(x: int, y: int, duration: float) -> None:
    """Move the mouse to the specified x, y coordinates with tweening."""
    pyautogui.moveTo(x, y, duration=duration, tween=pyautogui.easeInOutQuad)


@mcp.tool()
def write_text(text: str, interval: float = 0.0) -> None:
    """Type the specified text with a delay between each key."""
    pyautogui.write(text, interval=interval)


@mcp.tool()
def press_key(key: str) -> None:
    """Simulate pressing a single key."""
    pyautogui.press(key)


@mcp.tool()
def hold_and_write_keys(hold: str, keys: list[str]) -> None:
    """
    Hold a key and write a sequence of keys.
    example: hold_and_write_keys('shift', ['a', 'b', 'c'])
    """
    pyautogui.keyDown(hold)
    pyautogui.write(keys)
    pyautogui.keyUp(hold)


@mcp.tool()
def execute_hotkey(*keys: str) -> None:
    """
    Simulate pressing a combination of keys.
    example: execute_hotkey('ctrl', 'c')
    """
    pyautogui.hotkey(*keys)


@mcp.tool()
def get_keyboard_keys() -> list[str]:
    """Get a list of all keyboard keys."""
    return ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
            ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
            '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
            'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
            'browserback', 'browserfavorites', 'browserforward', 'browserhome',
            'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
            'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
            'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
            'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
            'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
            'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
            'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
            'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
            'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
            'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
            'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
            'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
            'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
            'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
            'command', 'option', 'optionleft', 'optionright']

@mcp.tool()
def windows_prompt(message: str) -> str:
    """Show a prompt message box. example: windows_prompt('Enter your name')"""
    return pyautogui.prompt(text=message) or ''


@mcp.tool()
def screenshot(filename: str = "screenshot.png") -> str:
    """Take a screenshot and save it to a file."""
    image = pyautogui.screenshot()
    image.save(filename)
    return path.abspath(filename)

if __name__ == "__main__":
    mcp.run()
