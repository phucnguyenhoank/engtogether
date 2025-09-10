from pydantic import BaseModel


class CoEdITRequest(BaseModel):
    instruction: str = "Rewrite to make this easier to understand"
    text: str

    def generate_command(self) -> str:
        return self.instruction + ": " + self.text


class CoEdITResponse(BaseModel):
    instruction: str
    old_text: str
    improved_text: str
