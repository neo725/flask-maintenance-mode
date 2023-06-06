const express = require('express')

// Constants
const PORT = 3000
const HOST = '0.0.0.0'

const app = express()
app.get('/', (req, res) => {
  // Customize the response status and reason
  res.status(593).send('Status: Server Planned Maintenance')
})

app.listen(PORT, HOST, () => {
  console.log('Server is running on port 3000')
})
