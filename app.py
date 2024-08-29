from flask import Flask, request, jsonify

app = Flask(__name__)

video_titles = [
    "The Art of Coding",
    "Exploring the Cosmos",
    "Cooking Masterclass: Italian Cuisine",
    "History Uncovered: Ancient Civilizations",
    "Fitness Fundamentals: Strength Training",
    "Digital Photography Essentials",
    "Financial Planning for Beginners",
    "Nature's Wonders: National Geographic",
    "Artificial Intelligence Revolution",
    "Travel Diaries: Discovering Europe"
]

video_titles.sort()

def binary_search(video_titles, target):
    low = 0
    high = len(video_titles) - 1

    while low <= high:
        mid = (low + high) // 2
        if video_titles[mid] == target:
            return mid  # Return the index of the found video title
        elif video_titles[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # Return -1 if the target is not found

@app.route('/')
def home():
    return "testing"

@app.route('/search', methods=['GET'])
def search_video():
    queryy = request.args.get('title')

    if not queryy:
        return jsonify({"error": "Title query parameter is required"}), 400
    
    index = binary_search(video_titles, queryy)
    if index != -1:
        return jsonify({"title": video_titles[index], "index": index}), 200
    else:
        return jsonify({"message": "Video not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=8080)