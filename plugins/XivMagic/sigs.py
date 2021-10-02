from FFxivPythonTrigger.memory import BASE_ADDR
from FFxivPythonTrigger.text_pattern import find_unique_signature_point, find_unique_signature_address

sigs = {
    "do_text_command": {
        'call': find_unique_signature_address,
        'param': "48 89 5C 24 ?? 57 48 83 EC 20 48 8B FA 48 8B D9 45 84 C9",
        'add': BASE_ADDR,
    },
    "text_command_ui_module": {
        'call': find_unique_signature_point,
        'param': "48 8B 05 * * * * 48 8B D9 8B 40 14 85 C0",
        'add': BASE_ADDR,
    },
    "do_action": {
        'call': find_unique_signature_address,
        'param': "40 53 55 57 41 54 41 57 48 83 EC ? 83 BC 24 ? ? ? ? ?",
        'add': BASE_ADDR,
    },
    "do_action_location": {
        'call': find_unique_signature_address,
        'param': "44 89 44 24 ? 89 54 24 ? 55 53 57",
        'add': BASE_ADDR,
    },
    "action_manager": {
        'call': find_unique_signature_point,
        'param': "48 8D 0D * * * * E8 ? ? ? ? 8B F8 8B CF",
        'add': BASE_ADDR,
    },
}
