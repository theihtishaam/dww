# generator/prompt_analyzer.py
def analyze_prompt(prompt: str) -> dict:
    result = {"domains": [], "features": [], "clone_template": None}
    prompt_lower = prompt.lower()

    if "pubg clone" in prompt_lower or ("pubg" in prompt_lower and "clone" in prompt_lower):
        result["domains"].append("game")
        result["clone_template"] = "pubg_clone"
    if "nord vpn clone" in prompt_lower or ("vpn" in prompt_lower and "clone" in prompt_lower):
        result["domains"].append("vpn")
        result["clone_template"] = "nord_vpn_clone"
    if "custom website" in prompt_lower or ("website" in prompt_lower and "movie" in prompt_lower):
        result["domains"].append("web")
        result["clone_template"] = "movie_website"
    
    if "game" in prompt_lower and result["clone_template"] is None:
        result["domains"].append("game")
    if "mobile" in prompt_lower or "app" in prompt_lower:
        result["domains"].append("mobile")
    if "web" in prompt_lower or "website" in prompt_lower:
        result["domains"].append("web")
    if "python" in prompt_lower:
        result["domains"].append("python")
    
    if "chat" in prompt_lower:
        result["features"].append("chat")
    if "update" in prompt_lower:
        result["features"].append("update")
    if "complex" in prompt_lower or "intelligent" in prompt_lower:
        result["features"].append("advanced_logic")
    
    return result
