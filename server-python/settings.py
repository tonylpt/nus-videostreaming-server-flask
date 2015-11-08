DB_URI = 'mysql://team03_15:jTevjFfpZdTYTTy@localhost:3306/team03_15_db?charset=utf8'

# Ensures that all nodes use the same cache server when clustering
USE_CACHE_FOR_POLLING = True

# Use either 'SIMPLE', or 'MEMCACHED'
CACHE_BACKEND = 'MEMCACHED'

# Memcached
MEMCACHED_HOST_PORT = 'localhost:11211'

SUPER_USERS = {
    "tony": "whoami",
}
