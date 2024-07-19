import gradio as gr

def greet(name):
    return f"Hello {name}!"

def start_server():
    iface = gr.Interface(fn=greet, inputs="text", outputs="text")
    iface.launch()

if __name__ == "__main__":
    start_server()
