const hapi = require('hapi');
const Route = require('../routes');

const server = new hapi.Server();

server.connection({
  host: 'localhost',
  port: 8080,
});

server.route(Route);

server.start((error) => {
  if (error) console.log(error);

  console.log(`Server running at: ${server.info.uri}`);
});
