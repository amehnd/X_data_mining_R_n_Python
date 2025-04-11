# if (!require("devtools")) install.packages("devtools")
# devtools::install_github("ropensci/rtweet", upgrade = "never")

# used just once 


library(dplyr)
library(ggplot2)
library(stringr)
library(tm)
library(wordcloud)
library(rtweet)
#library(twitteR)
library(languageserver)
install.packages("dotenv")
library(dotenv)

dotenv::load_dot_env()

# No support by X_API for twitteR package 
# consumer_key <- Sys.getenv("CONSUMER_KEY")
# consumer_secret <- Sys.getenv("CONSUMER_SECRET")
# access_token <- Sys.getenv("ACCESS_TOKEN")
# access_secret <- Sys.getenv("ACCESS_SECRET")

# setup_twitter_oauth(consumer_key,consumer_secret,access_token,access_secret)

# NY_tweets = searchTwitter("Statue of Liberty", n = 100, lang='en', resultType = "recent")
# print(NY_tweets)

auth <- rtweet::rtweet_bot(
  api_key = Sys.getenv("API_KEY"),
  api_secret = Sys.getenv("API_SECRET"),
  access_token = Sys.getenv("ACCESS_TOKEN"),
  access_secret = Sys.getenv("ACCESS_SECRET")
)

# Monkey patch for rtweet bug in search_params
unlockBinding("search_params", asNamespace("rtweet"))
assign("search_params", function(q,
                                 type = "recent",
                                 include_rts = TRUE,
                                 geocode = NULL,
                                 lang = NULL,
                                 locale = NULL,
                                 since_id = NULL,
                                 max_id = NULL,
                                 until = NULL,
                                 retryonratelimit = FALSE,
                                 verbose = TRUE) {
  params <- list(
    q = q,
    result_type = type,
    include_entities = "true",
    lang = lang,
    locale = locale,
    count = 100L,
    since_id = since_id,
    max_id = if (is.null(max_id)) NULL else as.character(max_id),
    until = until
  )
  params <- params[!sapply(params, is.null)]
  return(params)
}, envir = asNamespace("rtweet"))
lockBinding("search_params", asNamespace("rtweet"))


NY_tweets <- search_tweets(
  "Statue of Liberty",
  n = 100,
  lang = "en",
  type = "recent",
  token = auth
)

print(NY_tweets$text)
