const mongoose = require("mongoose");

const messageSchema = mongoose.Schema({
  user_id: {
    type: Number,
  },
  username: {
    type: String,
    default: null,
  },
  first_name: {
    type: String,
  },
  last_name: {
    type: String,
  },
  chat_id: {
    type: Number,
  },
  chat_title: {
    type: String,
    // required: true,
  },
  chat_type: {
    type: String,
  },
  text: {
    type: String,
  },
  date: {
    type: Date,
  },
  platform: {
    type: String,
  },
  isBot: {
    type: String,
  },
});

const messageModel = mongoose.model("messageAnalysisData", messageSchema);

module.exports = messageModel;
