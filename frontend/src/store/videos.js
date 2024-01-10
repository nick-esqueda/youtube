import { customFetch } from "../utils";
import { normalizeOneLevel } from "./utils";

// ACTION VARIABLES ***************************************
const ADD_VIDEO = 'videos/ADD_VIDEO';
const LOAD_VIDEOS = 'videos/LOAD_VIDEOS';
const LOAD_ADDITIONAL_VIDEOS = 'videos/LOAD_ADDITIONAL_VIDEOS';
const REMOVE_VIDEO = 'videos/REMOVE_VIDEO';
const CLEAR_VIDEOS = 'videos/CLEAR_VIDEOS';

// ACTION CREATORS ****************************************
const addVideo = (video) => {
    return {
        type: ADD_VIDEO,
        video
    }
}

const loadVideos = (videos) => {
    return {
        type: LOAD_VIDEOS,
        videos
    }
}

const loadAdditionalVideos = (videos) => {
    return {
        type: LOAD_ADDITIONAL_VIDEOS,
        videos
    }
}

const removeVideo = (videoId) => {
    return {
        type: REMOVE_VIDEO,
        videoId
    }
}

export const clearVideosState = () => {
    return {
        type: CLEAR_VIDEOS
    }
}

// THUNK ACTION CREATORS **********************************
export const fetchVideo = (videoId) => async dispatch => {
    const res = await customFetch(`/api/videos/${videoId}/`);

    if (res.ok) {
        const video = await res.json();
        dispatch(addVideo(video));
        return video;
    }
}

export const fetchRandomVideos = (pageNum = 1) => async dispatch => {
    const res = await customFetch(`/api/videos/pages/${pageNum}/`);

    if (res.ok) {
        const videos = await res.json();
        if (pageNum === 1) dispatch(loadVideos(videos));
        else dispatch(loadAdditionalVideos(videos));
        return videos;
    }
}

export const fetchChannelsVideos = (channelId, pageNum = 1) => async dispatch => {
    const res = await customFetch(`/api/channels/${channelId}/videos/pages/${pageNum}/`);

    if (res.ok) {
        const videos = await res.json();
        if (pageNum === 1) dispatch(loadVideos(videos));
        else dispatch(loadAdditionalVideos(videos));
        return videos;
    }
}

export const createVideo = video => async dispatch => {
    const res = await customFetch(`/api/videos/`, {
        method: 'POST',
        body: JSON.stringify(video)
    });

    if (res.ok) {
        const newVideo = await res.json();
        dispatch(addVideo(newVideo));
        return newVideo;
    } else {
        const errors = await res.json();
        throw errors
    }
}

export const editVideo = video => async dispatch => {
    const res = await customFetch(`/api/videos/${video.id}/`, {
        method: "PATCH",
        body: JSON.stringify(video)
    });

    if (res.ok) {
        const editedVideo = await res.json();
        dispatch(addVideo(editedVideo));
        return editedVideo;
    }
}

export const deleteVideo = (videoId) => async dispatch => {
    const res = await customFetch(`/api/videos/${videoId}/`, {
        method: 'DELETE',
    });

    if (res.ok) {
        const data = await res.json();
        // if delete is authorized, data will be an integer (videoId)
        if (data.notAuthorized === undefined) {
            dispatch(removeVideo(videoId));
            return videoId;
        } else {
            console.error(data);
        }
    }
}

export const searchVideos = (query) => async (dispatch) => {
    const res = await fetch(`${process.env.REACT_APP_BASE_URL}/api/search?` 
        + new URLSearchParams({query}));
    
    if (res.ok) {
        const videos = await res.json();
        dispatch(loadVideos(videos));
        return videos;
    }
}


// REDUCER ************************************************
const videosReducer = (state = {}, action) => {
    switch (action.type) {
        case LOAD_VIDEOS: {
            return {
                ...normalizeOneLevel(action.videos)
            }
        }

        case LOAD_ADDITIONAL_VIDEOS: {
            return {
                ...state,
                ...normalizeOneLevel(action.videos)
            }
        }

        case ADD_VIDEO: {
            const video = action.video;
            const dateParts = video.createdAt.split(' ');
            video.createdAt = `${dateParts[2]} ${dateParts[1]}, ${dateParts[3]}`;
            
            return {
                ...state,
                [video.id]: video,
            }
        }

        case REMOVE_VIDEO: {
            const newState = {...state};
            delete newState[action.videoId];
            return newState;
        }
            
        case CLEAR_VIDEOS: {
            return {};
        }

        default:
            return state;

    }
}

export default videosReducer;
