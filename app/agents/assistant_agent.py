import time

from app.services.rag_service import RAGService


class AssistantAgent:

    @staticmethod
    def ask(question):

        start_time = time.time()

        try:

            answer = RAGService.ask(question)

            return {

                "agent": "Assistant",

                "status": "success",

                "question": question,

                "answer": answer,

                "execution_time": round(
                    time.time() - start_time,
                    2
                )

            }

        except Exception as e:

            return {

                "agent": "Assistant",

                "status": "error",

                "question": question,

                "answer": "",

                "message": str(e),

                "execution_time": round(
                    time.time() - start_time,
                    2
                )

            }