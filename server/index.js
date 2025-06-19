const express = require("express");
const cors = require("cors");
const mongoose = require("mongoose");
const axios = require("axios");
const PORT = 5000;
const app = express();
app.use(express.json());
app.use(cors());
const messageRouter = require("./routes/messageRoutes");

mongoose
  .connect(
    "mongodb+srv://mavinash422:gfcz0io0dke50Xmb@cluster0.cj5pp.mongodb.net/analysisData?retryWrites=true&w=majority&appName=Cluster0"
  )
  .then(() => {
    console.log("Db Connected");
  })
  .catch((e) => {
    console.error(e);
  });

const schema = mongoose.Schema({
  userId: {
    type: String,
    required: true,
  },
  ip: {
    type: String,
    required: true,
  },
  country: {
    type: String,
  },
  city: {
    type: String,
  },
  latitude: {
    type: String,
  },
  longitude: {
    type: String,
  },
  isp: {
    type: String,
  },
  timezone: {
    type: String,
  },
  country_flag: {
    type: String,
  },
  createdAt: {
    type: Date,
    default: Date.now,
  },
});

const model = mongoose.model("ips", schema);

app.use("/api", messageRouter);

app.get("/", async (req, res) => {
  // const { data } = await axios.post(
  //   "http://localhost:5173/fetch_posts_by_hashtag",
  //   {
  //     hashtag: "sea",
  //   }
  // );
  // res.send(data);
  const { data } = await axios.post("http://localhost:5173/message_perp", {
    username: "___.dipesh_26",
  });
});

app.get("/get_lats_longs", async (req, res) => {
  try {
    // Select only the 'latitude' and 'longitude' fields from the documents
    const data = await model.find({}, { latitude: 1, longitude: 1, _id: 0 });

    // Log the retrieved data to the console
    console.log(data);

    // Send the data as a JSON response
    res.json(data);
  } catch (error) {
    console.error("Error fetching data:", error);
    res.status(500).send("Internal Server Error");
  }
});

app.listen(PORT, () => {
  console.log(`Server running on ${PORT}`);
});
