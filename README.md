# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Capstone Project: Song Recommender

### **Try Out Song Recommebder Streamlit Application by clicking the link below.**
# [Song Recommender](streamlit link)
Project management and planning documentation is done via Github Projects here: [githublink?]

<br>


<br>

## Content Directory:
- [Background](#Background)
- [Problem Statement](#Problem-Statement)
- [Data Collection](#Data-Collection)
- [Modeling](#Modeling)
- [Key Recommendations](#Key-Recommendations)

<br>


## Background



<br>



## Problem Statement


<br>

---

## Datasets:
* [`30000_spotify_songs.csv`](30000_spotify_songs.csv): Dataset of 30000 Spotify songs taken from [30000 Spotify Songs from Joakim Arvidsson](https://www.kaggle.com/datasets/joebeachcapital/30000-spotify-songs?select=spotify_songs.csv)

<br>

## Data Dictionary
| Feature | Type | Description |
| :--- | :---  | :---|
| track_id | object | Song unique ID |
| track_name | object  |  Song Name |
| track_artist | object |  Song Artist |
| track_popularity | int64   | Song Popularity (0-100) where a higher value represents being more popular |
| track_album_id | object  | Song Album unique ID |
| track_album_name | object  | Song Album name |
| track_album_release_date | object | Song Album release date |
| playlist_name | object  | Name of playlist |
| playlist_id | object  | Playlist ID |
| playlist_genre | object  | Playlist genre |
| playlist_subgenre | object  | Playlist subgenre |
| danceability | float64  | Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable. |
| energy | float64 | Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. For example, death metal has high energy, while a Bach prelude scores low on the scale. Perceptual features contributing to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy. |
| key | int64   | The estimated overall key of the track. Integers map to pitches using standard Pitch Class notation . E.g. 0 = C, 1 = C♯/D♭, 2 = D, and so on. If no key was detected, the value is -1. |
| loudness | float64  | The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track and are useful for comparing relative loudness of tracks. Loudness is the quality of a sound that is the primary psychological correlate of physical strength (amplitude). Values typical range between -60 and 0 db. |
| mode | int64   | Mode indicates the modality (major or minor) of a track, the type of scale from which its melodic content is derived. Major is represented by 1 and minor is 0. |
| speechiness | float64  | The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. Values above 0.66 describe tracks that are probably made entirely of spoken words. Values between 0.33 and 0.66 describe tracks that may contain both music and speech, either in sections or layered, including such cases as rap music. Values below 0.33 most likely represent music and other non-speech-like tracks. |
| acousticness | float64  | A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic. |
| instrumentalness | float64 | Predicts whether a track contains no vocals. "Ooh" and "aah" sounds are treated as instrumental in this context. Rap or spoken word tracks are clearly "vocal". The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. Values above 0.5 are intended to represent instrumental tracks, but confidence is higher as the value approaches 1.0. |
| liveness | float64  | Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live. A value above 0.8 provides strong likelihood that the track is live. |
| valence | float64  | A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry). |
| tempo | float64  | The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration.  |
| duration_ms | int64   | Duration of song in millisecondsn |

<br>

[pie chart of genres/subgenres?]

[histogram showing distribution across 'danceability'?]


<br>
<br>

## Data Collection


(taken from Kaggle)

(transforming object-variables 'playlist_genre' and 'playlist_subgenre' into arrays)

(dropping object variables, merge 'playlist_genre' and 'playlist_subgenre' into arrays with float64 variables)



## Modeling

[Picture/Summary for explaining cosine similarity]

Following the data preprocessing stage, the preprocessed dataset was fed into a pipeline of five classification models: **logistic regression, random forest classifier, XGBoost, Adaboost, and Voting Classifier**. These models were carefully chosen based on their respective strengths and suitability for the classification task at hand. The use of multiple models allowed us to leverage their individual capabilities and ensemble them to make more robust predictions.

Through this approach, we aimed to enhance the quality and reliability of our classification results, enabling us to make informed decisions based on the predictions generated by the ensemble of models.


<br>
<br>

## Summary of Model Perforamance

|  | Train Accuracy | Test Accuracy | Train F1 Score | Test F1 Score |
|---|---|---|---|---|
| **Null Model <br>(Baseline Model)** | 0.5 | 0.5 | 0.5 | 0.5 |
| **??** | **??** | **??** | **??** | ??** |
| **Logistic Regression** | 0.9983 | 0.9960 | 1.0 | 0.9958 |
| **XGBoost Classifier** | 0.9983 | 0.9960 | 1.0 | 0.9958 |
| **AdaBoost Classifier** | 0.9965 | 0.9960 | 1.0 | 0.9957 |

<br>

## Key Insights and Recommendations?

## Key Recommendations

[Suggestions for improvements?]



<br>

