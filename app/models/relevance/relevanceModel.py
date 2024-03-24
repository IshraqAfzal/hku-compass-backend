import torch, numpy
from sklearn.metrics.pairwise import cosine_similarity
from scipy.special import softmax

def description_relevance(model, tokenizer, description, text):
    maxlength = max(len(description.split()), len(text.split()))
    # Tokenize and encode the texts using BERT tokenizer
    input_ids1 = tokenizer.encode(description, add_special_tokens=True, max_length=maxlength, truncation=True, padding='max_length')
    input_ids2 = tokenizer.encode(text, add_special_tokens=True, max_length=maxlength, truncation=True, padding='max_length')
    # Convert the input to PyTorch tensors
    input_ids1 = torch.tensor(input_ids1).unsqueeze(0)  # Add batch dimension
    input_ids2 = torch.tensor(input_ids2).unsqueeze(0)  # Add batch dimension
    # Get BERT embeddings for the texts
    with torch.no_grad():
        outputs1 = model(input_ids1)
        embeddings1 = outputs1.last_hidden_state
        outputs2 = model(input_ids2)
        embeddings2 = outputs2.last_hidden_state
    # Convert embeddings to NumPy arrays
    embeddings1 = embeddings1[0].numpy()
    embeddings2 = embeddings2[0].numpy()
    # Calculate cosine similarity between the embeddings
    similarity = cosine_similarity(embeddings1, embeddings2)
    return similarity[0][0]

def action_verbs_count(nlp, text):
    action_verbs = [
        "Prepare", "Plan", "Organize", "Attend", "Engage", "Review", "Practice", "Seek", "Network", "Adapt",
        "Balance", "Stay Motivated", "Reflect", "Utilize", "Manage", "Take Notes", "Stay Informed", "Achieve", "Learn", "Understand",
        "Analyze", "Discuss", "Participate", "Collaborate", "Research", "Experiment", "Adapt", "Focus", "Prioritize",
        "Problem-solve", "Communicate", "Listen", "Support", "Guide", "Clarify", "Simplify", "Demonstrate", "Encourage", "Coach",
        "Motivate", "Inspire", "Challenge", "Evaluate", "Monitor", "Assess", "Evaluate", "Revise", "Improve", "Master", "Apply",
        "Share", "Exchange", "Connect", "Relate", "Collaborate", "Integrate", "Assist", "Serve", "Offer", "Recommend", "Suggest",
        "Advise", "Mentor", "Guide", "Help", "Empower", "Assist", "Familiarize", "Inform", "Direct", "Influence", "Lead", "Inspire",
        "Encourage", "Promote", "Facilitate", "Foster", "Advocate", "Support", "Nurture", "Empathize", "Inspire", "Motivate",
        "Resolve", "Tackle", "Overcome", "Face", "Conquer", "Manage", "Maintain", "Handle", "Address", "Cope", "Adapt", "Flourish",
        "Thrive", "Excel", "Achieve", "Succeed", "Triumph"
    ]
    doc = nlp(text)
    verbs_in_text = [token.text for token in doc if token.text in action_verbs]
    score = len(verbs_in_text)
    return score

def length(text):
    base = "Introduction to object-oriented programming; abstract data types and classes; inheritance and polymorphism; object-oriented program design; Java language and its program development environment; user interfaces and GUI programming; collection class and iteration protocol; program documentation. Prerequisite: ENGG1340 or COMP2113 or COMP2123 Mutually exclusive with: ELEC2543 Assessment: 50% continuous assessment, 50% examination"
    # Calculate the score for the new text
    score = len(text)/len(base)
    return score

def roberta_polarity_scores(model, tokenizer, text):
    encoded_text = tokenizer(text, return_tensors='pt')
    output = model(**encoded_text)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    scores_dict = {
        'roberta_neg': scores[0],
        'roberta_neu': scores[1],
        'roberta_pos': scores[2]
    }
    total = scores_dict['roberta_neg'] + scores_dict['roberta_pos']
    return total
