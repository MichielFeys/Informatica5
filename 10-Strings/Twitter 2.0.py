tweet = input('geef tweet: ')

i_hashtag = tweet.find('#')

while i_hashtag != -1:
    # tweet afknappen net na #
    tweet = tweet[i_hashtag + 1:]
    i_spatie = tweet.find(' ')
    # hashtag uitknippen ( en printen)
    print(tweet[:i_spatie])
    #terug op zoek naar #
    i_hashtag = tweet.find('#')
