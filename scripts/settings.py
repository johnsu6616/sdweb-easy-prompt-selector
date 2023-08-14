from modules import script_callbacks, shared

def on_ui_settings():
    shared.opts.add_option("eps_enable_save_raw_prompt_to_pnginfo", shared.OptionInfo(False, "將原始提示保存到 pnginfo", section=("easy_prompt_selector", "EasyPromptSelector")))

script_callbacks.on_ui_settings(on_ui_settings)
