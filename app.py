import gradio as gr

with gr.Blocks(title="Hello World") as demo:
    gr.Markdown("# Hello World 👋")

if __name__ == "__main__":
    demo.launch()
