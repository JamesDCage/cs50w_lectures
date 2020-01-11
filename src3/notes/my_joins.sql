SELECT P.name,
       F.origin,
       F.destination,
       F.duration
FROM   passengers AS P
       JOIN flights AS F
         ON P.flight_id = F.id ;


Above is verbose. Can remove a lot in this situation:

SELECT name,
       origin,
       destination,
       duration
FROM   passengers
       JOIN flights
         ON flight_id = flights.id ;