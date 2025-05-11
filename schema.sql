drop table if exists collected;
drop table if exists movies;
drop table if exists users;

create table users (
  id integer primary key,
  user text unique not null,
  check(user != '')
);

create table movies (
  id integer primary key,
  movie text unique not null,
  info text,
  check(movie != '')
);

create table collected (
  id integer primary key,
  user integer references users not null,
  movie integer references movies not null,
  rating integer not null default 0,
  check(rating between 0 and 5),
  unique(user, movie)
);
