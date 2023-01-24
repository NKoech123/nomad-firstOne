import { PrismaClient } from '@prisma/client'
import express from 'express'

const prisma = new PrismaClient()
const app = express()

async function main() {
  // ... your Prisma Client queries will go here
  const newUser = await prisma.user.create({
    data: {
        name: 'Alice',
        email: 'alice@gmail.com',
        posts: {
            create:{
                title: 'Hello World',
            },
        },
    }
  })
  console.log('Created new user', newUser)

  const allUsers = await prisma.user.findMany({
    include: {posts: true},
  })
  console.log('All Users,')
  console.dir(allUsers, { depth: null })

}

main()
  .catch((e) => console.error(e))
  .finally(async () => await prisma.$disconnect())


app.use(express.json())

// ... your REST API routes will go here
app.get('/users', async (req, res) => {
    const users = await prisma.user.findMany()
    res.json(users)
  })

app.listen(3000, () =>
  console.log('REST API server ready at: http://localhost:3000'),
)