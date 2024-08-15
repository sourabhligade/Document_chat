from rest_framework.decorators import api_view
from rest_framework.response import Response

# Dummy implementations for chat start and message
@api_view(['POST'])
def start_chat(request):
    asset_id = request.data.get('asset_id')
    if asset_id:
        # Dummy chat thread ID generation
        chat_thread_id = "thread123"
        return Response({'chat_thread_id': chat_thread_id})
    return Response({'error': 'Asset ID required'}, status=400)

@api_view(['POST'])
def send_message(request):
    chat_thread_id = request.data.get('chat_thread_id')
    user_message = request.data.get('message')
    if chat_thread_id and user_message:
        # Dummy response generation
        agent_response = "This is a dummy response."
        return Response({'response': agent_response})
    return Response({'error': 'Chat thread ID and message required'}, status=400)

@api_view(['GET'])
def chat_history(request, chat_thread_id):
    # Dummy chat history
    history = [
        {"message": "Hello, how can I help you?", "sender": "agent"},
        {"message": "Tell me more about the document.", "sender": "user"}
    ]
    return Response({'history': history})
