from pydantic import BaseModel

INSTRUCTION = "Fix grammar and coherence"

class CoEdITRequest(BaseModel):
    instruction: str = INSTRUCTION
    text: str

    def generate_command(self) -> str:
        return self.instruction + ": " + self.text

class CoEdITResponse(BaseModel):
    instruction: str = INSTRUCTION
    old_text: str
    improved_text: str
