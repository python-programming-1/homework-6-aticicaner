import csv
import pprint


def get_video_data():
    """this function reads from a .csv file and converts the data into a list of dictionaries.
     each item in the list is a dictionary of a specific videos and their attributes."""

    vid_data = []
    with open('USvideos.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            if len(row) == 16:
                vid_dict = {'video_id': row[0],
                            'trending_date': row[1],
                            'title': row[2],
                            'channel_title': row[3],
                            'category_id': row[4],
                            'publish_times': row[5],
                            'tags': row[6],
                            'views': row[7],
                            'likes': row[8],
                            'dislikes': row[9],
                            'comment_count': row[10],
                            'thumbnail_link': row[11],
                            'comments_disabled': row[12],
                            'ratings_disabled': row[13],
                            'video_error': row[14],
                            'description': row[15]
                            }
                vid_data.append(vid_dict)
    return vid_data


def print_data(data):
    for entry in data:
        pprint.pprint(entry)


def get_most_popular_and_least_popular_channel(data):
    """ fill in the Nones for the dictionary below using the vid data """
    most_popular_and_least_popular_channel = {'most_popular_channel': None, 'least_popular_channel': None, 'most_pop_num_views': None,
                                              'least_pop_num_views': None}

    # temporary dict to keep channel names and their total views
    temp_most_popular = {}

    for item in data[1:]:
        temp_most_popular.setdefault(item['channel_title'], 0)
        temp_most_popular[item['channel_title']] += int(item['views'])

    highest_name = ""
    highest = 0
    lowest_name= ""
    lowest = 500000000000 # unreasonably high starting point to start comparison

    # look for highest and lowest view total channels in temp_most_popular dictionary
    # parse once while looking for both o(N) time complexity
    for field, possible_values in temp_most_popular.items():
        if possible_values > highest:
            highest_name = field
            highest = possible_values
        elif possible_values < lowest:
            lowest_name = field
            lowest = possible_values

    # assign values to output
    most_popular_and_least_popular_channel['most_popular_channel'] = highest_name
    most_popular_and_least_popular_channel['most_pop_num_views'] = highest
    most_popular_and_least_popular_channel['least_popular_channel'] = lowest_name
    most_popular_and_least_popular_channel['least_pop_num_views'] = lowest
    return most_popular_and_least_popular_channel


def get_most_liked_and_disliked_channel(data):
    """ fill in the Nones for the dictionary below using the bar party data """

    most_liked_and_disliked_channel = {'most_liked_channel': None, 'num_likes': None, 'most_disliked_channel': None, 'num_dislikes': None}

    temp_most_liked = {}
    temp_most_disliked = {}

    # parses data once split it to two dictionaries
    for item in data[1:]:
        temp_most_liked.setdefault(item['channel_title'], 0)
        temp_most_liked[item['channel_title']] += int(item['likes'])
        temp_most_disliked.setdefault(item['channel_title'], 0)
        temp_most_disliked[item['channel_title']] += int(item['dislikes'])

    liked_name = ""
    likes_count = 0

    # look for most liked channel
    for field, possible_values in temp_most_liked.items():
        if possible_values > likes_count:
            liked_name = field
            likes_count = possible_values

    # assign values to output
    most_liked_and_disliked_channel['most_liked_channel'] = liked_name
    most_liked_and_disliked_channel['num_likes'] = likes_count

    disliked_name = ""
    dislikes_count = 0

    #look for the most disliked channel
    for field, possible_values in temp_most_disliked.items():
        if possible_values > dislikes_count:
            disliked_name = field
            dislikes_count = possible_values

    # assign values to output
    most_liked_and_disliked_channel['most_disliked_channel'] = disliked_name
    most_liked_and_disliked_channel['num_dislikes'] = dislikes_count


    return most_liked_and_disliked_channel


if __name__ == '__main__':
    vid_data = get_video_data()

    # uncomment the line below to see what the data looks like
    # print_data(vid_data)

    popularity_metrics = get_most_popular_and_least_popular_channel(vid_data)

    like_dislike_metrics = get_most_liked_and_disliked_channel(vid_data)

    print('Popularity Metrics: {}'.format(popularity_metrics))
    print('Like Dislike Metrics: {}'.format(like_dislike_metrics))
