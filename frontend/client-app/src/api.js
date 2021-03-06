const axios = require('axios')
const devServer = 'http://127.0.0.1:8000/api/';

export  const getPosts = async ()=>{
    const response = await axios.get('http://127.0.0.1:8000/api/post');
    console.log("This response:" + JSON.stringify(response.data));
  }

export const createTag = async (tagName,tagParentid)=>{
    var response = await axios.post(devServer + 'createtag',{
        name:tagName,
        tag:tagParentid,
    })
    return response;
}

export const login = async (email,password)=>{
    var response = await axios.post(devServer + 'login',{
        email:email,
        password:password,
    });
    return response;
}

export const signup = async (formdata)=>{
    var response = await axios.post(devServer + 'signup',formdata,
    {
        headers: {
            'Content-Type': 'multipart/form-data'
            }
            });
    return response;
}

export const approvepost = async (post_id)=>{
    var response = await axios.post(devServer + 'approvepost',{
        post_id:post_id,
    });
    return response;
}

export const banuser = async (moderatorid,userid)=>{
    var response = await axios.post(devServer + 'banuser',{
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
    var response = await axios.get(devServer + 'saved/' + userid);
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

export const pendingApprovals = async()=>{
    var response = await axios.get(devServer + 'pendingapprovals');
    return response;
}

export const savePost = async(user_id,post_id)=>{
    var response = await axios.post(devServer + 'savepost',{
        user_id:user_id,
        post_id:post_id,
    });
    return response;
}

export const updateRole = async(user_id,role)=>{
    var response = await axios.post(devServer + 'updaterole',{
        user_id:user_id,
        role:role,
    });
    return response;
}

export const likePost = async(user_id,post_id)=>{
    var response = await axios.post(devServer + 'likepost',{
        user_id:user_id,
        post_id:post_id,
    });
    return response;
}

export const verifyComment = async(comment_id,user_id)=>{
    var response = await axios.post(devServer + 'verifycomment',{
        user_id:user_id,
        comment_id:comment_id,
    });
    return response;
}

export const reportComment = async(comment_id,user_id)=>{
    var response = await axios.post(devServer + 'reportcomment',{
        user_id:user_id,
        comment_id:comment_id,
    });
    return response;
}

export const reportPost = async(user_id,post_id)=>{
    var response = await axios.post(devServer + 'reportpost',{
        user_id:user_id,
        post_id:post_id,
    });
    return response;
}

export const getLatestPosts = async()=>{
    var response = await axios.get(devServer + 'latest');
    return response;
}

export const getMostCommentedPosts = async()=>{
    var response = await axios.get(devServer + 'top');
    return response;
}

export const getPostSuggestions = async(search,search_type)=>{
    var response = await axios.post(devServer + 'suggest',{
        search_term:search,
        search_type:search_type,

    });
    return response;
}

export const getFilteredPosts = async(search_term,search_type)=>{
    var response = await axios.post(devServer + 'search',{
        search_term:search_term,
        search_type:search_type,
    });
    return response;
}

export const uploadComment = async(text,userid,postid)=>{
    var response = await axios.post(devServer + 'uploadcomment',{
        text:text,
        user_id:userid,
        post_id:postid,
    });
    return response;
}

export const uploadPost = async(formdata)=>{
    var response = await axios.post(devServer + 'uploadpost',formdata,
    {
      headers: {
          'Content-Type': 'multipart/form-data'
      }
    });
    return response;
}

export const getReportedPosts = async()=>{
    var response = await axios.get(devServer + 'reportedposts');
    return response;
}