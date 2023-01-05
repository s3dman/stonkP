import dearpygui.dearpygui as dpg
import config
import theme

import mainpage

def loginpage():
    ui = { "l":{}, "b":{} }

    with dpg.window(tag="loginpage",width=config.W, height=config.H, no_resize=True , no_move=False, no_close=True, no_collapse=True):
        ui["l"]["informer"] = dpg.add_text("this is the loginpage")
        ui["b"]["mainpage"] = dpg.add_button(label="go to mainpage",callback=lambda:
                       config.window_handler("loginpage",mainpage.mainpage))
        dpg.bind_item_font(ui["l"]["informer"],theme.font_registry.JBM[25])
    dpg.set_primary_window('loginpage',True)