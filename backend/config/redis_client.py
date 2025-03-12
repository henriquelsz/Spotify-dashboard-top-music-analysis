import redis
import os

#Connecting to Redis
redis_client = redis.Redis(
    host = os.getenv("REDIS_HOST", "localhost"),
    port = int(os.getenv("REDIS_PORT", 6379)),
    decode_responses = True #return string insteand bytes
)

def store_token_to_redis(access_token: str, expires_in: int, *args):
    #save token in the redis with the expiration time
    redis_client.setex(f"spotify_token", expires_in, access_token)

def get_token_from_redis(*args):
    return redis_client.get("spotify_token")

def delete_token_from_redis(*args):
    redis_client.delete("spotify_token")