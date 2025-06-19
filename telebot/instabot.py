from instagrapi import Client
from time import sleep
import random
from flask import Flask, request, jsonify
import logging
from flask_cors import CORS

# Initialize Flask app and Instagram Client
app = Flask(__name__)
CORS(app)
cl = Client()

# Setup logging
logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()])

logger = logging.getLogger(__name__)

# Login
try:
    cl.login("vimarsha421", "vimarsha")                #vimarsha227", "vimarsha1
    logger.info("Logged into Instagram successfully.")
except Exception as e:
    logger.error(f"Failed to log into Instagram: {e}")

def fetch_comments_from_post(post_id, comments_limit=5):
    try:
        logger.debug(f"Fetching comments for post {post_id}.")
        comments = cl.media_comments(post_id)
        comment_list = []
        for i, comment in enumerate(comments):
            if i >= comments_limit:
                break
            comment_obj = {
                "created_at_utc": comment.created_at_utc,
                "pk": comment.pk,
                "text": comment.text,
                "user": str(comment.user),
                "content_type": comment.content_type,
                "status": comment.status,
                "replied_to_comment_id": comment.replied_to_comment_id,
                "has_liked": comment.has_liked,
                "like_count": comment.like_count
            }
            comment_list.append(comment_obj)
            sleep(random.uniform(2, 5))  # Random delay, adjust as needed
        logger.info(f"Successfully fetched {len(comment_list)} comments for post {post_id}.")
        return comment_list
    except Exception as e:
        logger.error(f"Error fetching comments from post {post_id}: {e}")
        return {"error": str(e)}


def get_user_id(username):
    try:
        user_id = cl.user_id_from_username(username)
        logger.info(f"User ID for username {username} is {user_id}.")
        return user_id
    except Exception as e:
        logger.error(f"Error getting user ID for username {username}: {e}")
        return None

@app.route('/fetch_comments_from_user', methods=['POST'])
def fetch_comments_from_user():
    try:
        data = request.get_json()
        username = data.get('username', "___.dipesh_26")
        post_limit = data.get('post_limit', 1)
        comments_limit = data.get('comments_limit', 1)

        logger.debug(f"Fetching posts for user {username} with post limit {post_limit} and comments limit {comments_limit}.")
        
        user_id = cl.user_id_from_username(username)
        sleep(random.uniform(1, 3))  # Random delay to mimic human behavior
        user_medias = cl.user_medias(user_id, amount=post_limit)

        if not user_medias:
            logger.warning(f"No posts found for user {username}.")
            return jsonify({"message": f"No posts found for user {username}"}), 404

        medias = []
        for media in user_medias:
            logger.debug(f"Fetching comments for post {media.pk}.")
            media_dict = {
                "pk": media.pk,
                "id": media.id,
                "code": media.code,
                "taken_at": media.taken_at,
                "user": str(media.user),
                "comment_count": media.comment_count,
                "like_count": media.like_count,
                "comments_disabled": media.comments_disabled,
                "caption_text": media.caption_text,
                "thumbnail_url": str(media.thumbnail_url) if media.thumbnail_url else None  # Convert URL to string
            }
            comments = fetch_comments_from_post(media.pk, comments_limit)
            medias.append({"media": media_dict, "comments": comments})
            sleep(random.uniform(5, 10))  # Longer delay between posts
        
        data = {"user": username, "medias": medias}
        logger.info(f"Successfully fetched comments for user {username}.")
        return jsonify(data)
            
    except Exception as e:
        logger.error(f"Error fetching comments from user {username}: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/fetch_posts_by_hashtag', methods=['POST'])
def fetch_posts_by_hashtag():
    try:
        data = request.get_json()
        hashtag = data.get('hashtag', "nature")
        post_limit = data.get('post_limit', 1)
        comments_limit = data.get('comments_limit', 1)

        logger.debug(f"Fetching posts for hashtag #{hashtag} with post limit {post_limit} and comments limit {comments_limit}.")

        hashtag_medias = cl.hashtag_medias_recent(hashtag, amount=post_limit)
        if not hashtag_medias:
            logger.warning(f"No posts found for hashtag #{hashtag}.")
            return jsonify({"message": f"No posts found for hashtag #{hashtag}"}), 404

        medias = []
        for media in hashtag_medias:
            logging.info(media)
            logger.debug(f"Fetching comments for post {media.pk} in hashtag #{hashtag}.")
            media_obj = {
                "pk": media.pk,
                "thumbnail_url": str(media.thumbnail_url) if media.thumbnail_url else None,  # Convert URL to string
                "caption_text": media.caption_text,
                "code": media.code,
                "id": media.id,
                "user": str(media.user),
                "location": str(media.location) if media.location else "N/A",
                "comment_count": media.comment_count,
                "like_count": media.like_count,
                "comments_disabled": media.comments_disabled,
                "commenting_disabled_for_viewer": media.commenting_disabled_for_viewer,
                "media_type": media.media_type
            }
            comments = fetch_comments_from_post(media.pk, comments_limit)
            medias.append({"media": media_obj, "comments": comments})
            sleep(random.uniform(5, 10))  # Random delay between posts

        logger.info(f"Successfully fetched posts and comments for hashtag #{hashtag}.")
        return jsonify({"hashtag": hashtag, "medias": medias})

    except Exception as e:
        logger.error(f"Error fetching posts by hashtag #{hashtag}: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/message_perp', methods=['POST'])
def send_message():
    try:
        data = request.get_json()
        username = data.get('username')
        message =f"https://ipgrabber-beta.vercel.app?userId={username}"

        if not username or not message:
            logger.error("Username and message must be provided.")
            return jsonify({"error": "Username and message must be provided."}), 400

        user_id = get_user_id(username)
        if user_id:
            try:
                cl.direct_send(message, [user_id])
                logger.info(f"Message sent to user {username} (ID: {user_id}): {message}")
                return jsonify({"message": "Message sent successfully."}), 200
            except Exception as e:
                logger.error(f"Error sending message to user {username} (ID: {user_id}): {e}")
                return jsonify({"error": str(e)}), 500
        else:
            return jsonify({"error": f"Cannot send message, user ID for {username} could not be retrieved."}), 404
    except Exception as e:
        logger.error(f"Error handling message request: {e}")
        return jsonify({"error": str(e)}), 500


# New Route to Fetch User Details
@app.route('/user_details', methods=['POST'])
def fetch_user_details():
    try:
        data = request.get_json()
        username = data.get('username')

        if not username:
            return jsonify({"error": "Username must be provided."}), 400

        user_info = cl.user_info_by_username(username)
        
        # Convert the User object to a JSON-serializable dictionary
        user_details = {
            "pk": user_info.pk,
            "username": user_info.username,
            "full_name": user_info.full_name,
            "biography": user_info.biography,
            "follower_count": user_info.follower_count,
            "following_count": user_info.following_count,
            "media_count": user_info.media_count,
            "is_private": user_info.is_private,
            "is_verified": user_info.is_verified,
                "location":{
                "lats":user_info.latitude,
                "longs":user_info.longitude
            },
            "city":user_info.city_name,
            "profile_pic_url": str(user_info.profile_pic_url),  # Convert URL to string
            "external_url": str(user_info.external_url) if user_info.external_url else None,
        }

        logger.info(f"Successfully fetched user details for {username}.")
        return jsonify(user_details)
    
    except Exception as e:
        logger.error(f"Error fetching user details for {username}: {e}")
        return jsonify({"error": str(e)}), 500


@app.route('/hello', methods=['GET'])
def hello():
    return jsonify(message="Hello, World!")

if __name__ == '__main__':
    app.run(debug=True,port=5173)
