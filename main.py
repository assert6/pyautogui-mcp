# server.py
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
    if x is not None and y is not None:
        pyautogui.click(x, y)
    else:
        pyautogui.click()


@mcp.tool()
def move_mouse_relative(x_offset: int = 0, y_offset: int = 0) -> None:
    """Move the mouse relative to its current position."""
    pyautogui.move(x_offset, y_offset)


@mcp.tool()
def double_click_mouse() -> None:
    """Double click the mouse at its current position."""
    pyautogui.doubleClick()


@mcp.tool()
def move_mouse_with_tween(x: int, y: int, duration: float) -> None:
    """Move the mouse to the specified x, y coordinates with tweening."""
    pyautogui.moveTo(x, y, duration=duration, tween=pyautogui.easeInOutQuad)


@mcp.tool()
def type_text(text: str, interval: float = 0.25) -> None:
    """Type the specified text with a delay between each key."""
    pyautogui.write(text, interval=interval)


@mcp.tool()
def press_key(key: str) -> None:
    """Simulate pressing a single key."""
    pyautogui.press(key)


@mcp.tool()
def hold_and_write_keys(keys: list[str]) -> None:
    """Hold the shift key and write a sequence of keys."""
    pyautogui.keyDown('shift')
    pyautogui.write(keys)
    pyautogui.keyUp('shift')


@mcp.tool()
def execute_hotkey(*keys: str) -> None:
    """Simulate pressing a combination of keys."""
    pyautogui.hotkey(*keys)

if __name__ == "__main__":
    mcp.run()
