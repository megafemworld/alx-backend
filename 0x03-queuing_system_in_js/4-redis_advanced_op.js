import { createClient } from "redis";
const client = createClient();
client.on("connect", () => {
  console.log("Redis client connected to the server");
});
client.on("error", (error) => {
  console.error(`Redis client not connected to the server: ${error.message}`);
});

function hsetter(hash, key, value) {
  client.hset(hash, key, value, (err, reply) => {
    console.log(`Reply: ${reply}`);
    if (err) console.error(err);
  });
}

const cities = {
    Portland: 50,
    Seattle: 80,
    "New York": 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2
};

Object.entries(cities).forEach(([key, value]) => {
    hsetter("HolbertonSchools", key, value);
    });

client.hgetall("HolbertonSchools", (err, reply) => {
    console.log(reply);
    if (err) console.error(err);
});