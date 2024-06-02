from crewai_tools import BaseTool, PDFSearchTool

class MyCustomTool(BaseTool):
    name: str = "PDF RAG Tool"
    description: str = (
        "This tool allows for searching PDF content using a Retrieval-Augmented Generation approach."
    )

    def _run(self, argument: str) -> str:
        # Initialize the PDFSearchTool with the given configuration
        tool = PDFSearchTool(
            config=dict(
                llm=dict(
                    provider="groq",  # You can also use 'google', 'openai', 'anthropic', 'llama2', etc.
                    config=dict(
                        model="llama3-8b-8192",
                        # Uncomment and set the desired values if needed
                        # temperature=0.5,
                        # top_p=1,
                        # stream=True,
                    ),
                ),
                embedder=dict(
                    provider="groq",  # You can also use 'openai', 'ollama', etc.
                    config=dict(
                        model="models/embedding-001",
                        task_type="retrieval_document",
                        # title="Embeddings",
                    ),
                ),
            )
        )
        
        # Perform the search with the provided argument
        search_result = tool.search(argument)

        # Process the result and return the output
        return f"Search results: {search_result}"

# Example usage
#if __name__ == "__main__":
 #   my_tool = MyCustomTool()
  #  result = my_tool._run("Sample query to search in PDF")
   # print(result)
