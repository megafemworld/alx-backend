import { createClient } from 'redis';
const util = require('util');

const client = createClient();
client.on("connect", () => {
  console.log("Redis client connected to the server");
});

client.on("error", (error) => {
  console.error(`Redis client not connected to the server: ${error.message}`);
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (err, reply) => {
    console.log(`Reply: ${reply}`);
    if (err) console.error(err);
  });
}

const getAsync  = util.promisify(client.get).bind(client);
async function displaySchoolValue(schoolName) {
    try {
        const reply = await getAsync(schoolName);
        console.log(reply);
    } catch (error) {
        console.error(error);
    }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
