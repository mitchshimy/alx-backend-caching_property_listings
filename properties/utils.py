import logging
from django_redis import get_redis_connection

logger = logging.getLogger(__name__)

def get_redis_cache_metrics():
    """
    Retrieves Redis cache hit/miss statistics and calculates the hit ratio.
    Logs and returns a dictionary of metrics.
    """
    redis_conn = get_redis_connection("default")
    info = redis_conn.info("stats")

    hits = info.get("keyspace_hits", 0)
    misses = info.get("keyspace_misses", 0)

    total = hits + misses
    hit_ratio = (hits / total) if total > 0 else None

    metrics = {
        "keyspace_hits": hits,
        "keyspace_misses": misses,
        "hit_ratio": round(hit_ratio, 4) if hit_ratio is not None else "N/A"
    }

    logger.info(f"Redis Cache Metrics: {metrics}")
    return metrics
