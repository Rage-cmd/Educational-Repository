const axios = require('axios')
const devServer = 'http://127.0.0.1:8000/api/';

export  const getPosts = async ()=>{
    const response = await axios.get('http://127.0.0.1:8000/api/post');
    console.log("This response:" + JSON.stringify(response.data));
  }

export const uploadPost = async (postModel,userid)=>{
    var response = await axios.post(devServer + 'uploadpost',
    {
        post:postModel,
        userid:userid,
    })
    return response;
}

export const createTag = async (tagModel,userid)=>{
    var response = await axios.post(devServer + 'createtag',{
        tag:tagModel,
        userid:userid,
    })
    return response;
}

export const getCachedPosts = async ()=>{
    var response = await axios.get(devServer);
    return response;
}

export const login = async (email,password)=>{
    var response = await axios.post(devServer + 'login',{
        email:email,
        password:password,
    });
    return response;
}

export const signup = async (username,email,password)=>{
    var response = await axios.post(devServer + 'signup',{
        "username":username,
        "email":email,
        "password":password
    });
    return response;
}

export const postApproval = async (postid,userid)=>{
    var response = await axios.post(devServer + 'postapproval',{
        postid:postid,
        userid:userid,
    });
    return response;
}

export const banuser = async (moderatorid,userid)=>{
    var response = await axios.post(devServer + 'banUser',{
        moderatorid:moderatorid,
        user_id:userid,
    });
    return response;
}

export const unbanuser = async (moderatorid,userid)=>{
    var response = await axios.post(devServer + 'unbanuser',{
        moderatorid:moderatorid,
        user_id:userid,
    });
    return response;
}

export const getSavedPosts = async (userid)=>{
    var response = await axios.get(devServer + 'uploads/' + userid);
    return response;
}

export const getUserDetails = async (userid)=>{
    var response = await axios.get(devServer + 'user/'+userid);
    return response;
}

export const yourUploads = async (userid='u2')=>{
    var response = await axios.get(devServer + 'uploads/' + userid);
    return response;
}

export const upgradeUserLevel = async (adminid,userid)=>{
    var response = await axios.post(devServer + 'upgradeuserlevel',{
        adminid:adminid,
        userid:userid,
    });
    return response;
}

export const getSuggestion = async (suggestionModel)=>{
    var response = await axios.post(devServer + 'suggestion',{
        suggestion:suggestionModel,
    });
    return response;
}

export const search = async (searchModel)=>{
    var response = await axios.post(devServer + 'search',{
        search:searchModel,
    });
    return response;
}

export const notifications = async (userid)=>{
    var response = await axios.post(devServer + 'notifications',{
        userid:userid,
    });
    return response;
}

export const getAllUsers = async ()=>{
    var response = await axios.get(devServer + 'users');
    return response;
}

