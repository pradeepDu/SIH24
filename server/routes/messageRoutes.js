const express = require("express");
const messageModel = require("../models/messageAnalysis");
const router = express.Router();
const axios = require("axios");
router.post("/telegram", async (req, res, next) => {
  try {
    console.log(req.body);
    const { data } = await axios.get(
      `http://127.0.0.1:5001/predict?text=${req.body.text}`
    );
    console.log(data);
    let results;
    if (data.prediction == "1") {
      console.log("Stored");
      results = await messageModel.create({
        ...req.body,
        platform: "Telegram",
      });
    }
    res.status(200).json(data);
  } catch (e) {
    console.error(e);
    res
      .status(500)
      .json({ error: "An error occurred while processing your request." });
    next(e);
  }
});

module.exports = router;
