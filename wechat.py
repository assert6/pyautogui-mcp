from time import sleep
import pyperclip

from mcp.server.fastmcp import FastMCP
import pyautogui

# Create an MCP server
mcp = FastMCP("微信助手")
pyautogui.PAUSE = 0.05

@mcp.tool()
def open_wechat() -> None:
    """打开微信"""
    pyautogui.hotkey('command', 'space', interval=0.1)
    pyperclip.copy('微信')
    pyautogui.hotkey('command', 'v')
    pyautogui.press('enter')

@mcp.tool()
def search_friend(name: str) -> None:
    """搜索好友, 需要先打开微信"""
    pyautogui.hotkey('command', 'f')
    pyperclip.copy(name)
    pyautogui.hotkey('command', 'v')
    sleep(0.5)
    pyautogui.press('enter')

    # 如果当前已经在聊天窗口, 则需要切屏才能定位光标
    pyautogui.hotkey('command', 'tab')
    pyautogui.hotkey('command', 'tab')

@mcp.tool()
def send_message(message: str) -> None:
    """发送消息, 需要先搜索好友"""
    pyperclip.copy(message)
    pyautogui.hotkey('command', 'v')
    pyautogui.press('enter')

if __name__ == "__main__":
    mcp.run()
