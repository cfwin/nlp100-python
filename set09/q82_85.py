# on the interaction shell
mongo
> use [dbname]

#82 ensure index
db.tweets.ensureIndex({'url':1})
db.tweets.ensureIndex({'date':1})
db.tweets.ensureIndex({'user':1})
db.tweets.ensureIndex({'rt':1})
db.tweets.ensureIndex({'rep':1})
db.tweets.ensureIndex({'qt':1})

# check
db.tweets.stats()

#83 search by url
db.tweets.find({url:'http://twitter.com/****/statuses/***************'})

#84 search tweets replying particular tweet
db.tweets.finr({rep:'http://twitter.com/****/statuses/***************'}, {body:1})

#85 get the most retweeted 10 tweets
db.tweets.find({user:'tenkijp'}).sort({ref:-1}).limit(10)
