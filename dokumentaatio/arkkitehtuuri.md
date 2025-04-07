Alustava luokkakaavio. Tarkentuu sovelluksen kehittyessä.

```mermaid
  classDiagram
    User "1" -- "*" CollectedMovie
    Movie "1" -- "*" CollectedMovie

  class User {
    id
    name
  }

  class Movie {
    id
    name
    description
    image
  }

  class CollectedMovie {
    id
    movieId
    userId
    review
  }
```
