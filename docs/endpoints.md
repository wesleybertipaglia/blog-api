# 🪧 Endpoints

The API has the following endpoints:

### Auth

| Route                     | Action                               |
| :------------------------ | :----------------------------------- |
| `POST /auth`              | Sign-up                              |
| `POST /auth`              | Sign-in                              |
| `POST /auth`              | Sign-out                             |

### Profile

| Route                     | Action                               |
| :------------------------ | :----------------------------------- |
| `GET /profile`            | Get your profile                     |
| `PUT /profile`            | Update your profile                  |
| `DELETE /profile`         | Delete your profile                  |

### Users

| Route                     | Action                               |
| :------------------------ | :----------------------------------- |
| `GET /users`              | Get all products                     |
| `GET /users/:id`          | Get a specific product by ID         |

### Posts

| Route                        | Action                            |
| :--------------------------- | :-------------------------------- |
| `GET /posts`                 | Get all posts                     |
| `GET /posts/:id`             | Get a specific post by ID         |
| `POST /posts`                | Create a new post                 |
| `PUT /posts/:id`             | Update a post by ID               |
| `DELETE /posts/:id`          | Delete a post by ID               |