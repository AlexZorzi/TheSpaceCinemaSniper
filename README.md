<p align="center">
        <img src="https://user-images.githubusercontent.com/47613715/229617574-d0d8f850-b8ca-4a51-b4cb-67f5d5dd216d.png" width="300px">

</p>

## Demo


https://user-images.githubusercontent.com/47613715/229616897-1dd14fd6-dcbc-4f10-b516-8131161a3759.mp4


# TheSpace Cinema Sniper
Snipe any seats as soon as they come out

# Todos
- Full Statefull Objects
- Flow up to Payscreen
- Work with coupons
- Work in snipe mode 
- better cli UI
- web ui (?)
- obj works directly with json (?)

# Innerworkings

## How seats are choosen? (WIP)
We figure out the approximate center of all the seats (pink) then we create a list of every combination of subgroups we can make with the selected numbers of seats (3 in this case).
Then we pick the central seat and using the distance from two points formula we figure out the most suitable seats near the center.
![seatings](/docs/rankseats.png)

## What if the seats number is not odd?
We simply create an immaginary point in the middle of the two center seats and then calculate distance from there.
![even](/docs/even.png)


## Endpoints
- Main Url

        https://www.thespacecinema.it

- Login
        
       https://www.thespacecinema.it/security/loginajax

- Search

      https://www.thespacecinema.it/data/searchquery/

## Cookies

    
    ASP.NET_SessionId   3ymykyodjiowlxilfcbxlakn
    
    -- Extra After Login

    UserSessionId 6bbf16b9-f7e9-47c7-90d0-f5abe1a38fc1
    .ASPXAUTH   14FB3FCFEDCFD11EA95A120954D50EFDA3D141903DD32879FA34855A25BCA893EEDA55F8EE7B19B0D656AD3233460E63E062944FD68A5639EDE59768CA9ABD0E7ADB2BB6B7AC625E03766DE7A6C2E3C971DD390138E5EFF0D90CDB0125CBAC9BF6F3B9452F7280A0EDD2284CDDC5FBA65C01131CE9A9ADBE12A7F4301810C12035696C89078DBBF1BFF67B64AE63CA17BCDB51CBFEB8C66CF81119FC39E174BC1B93C91AD79139C241E280395D9A2337AD1D3537E59704EF7976C571F38B06231DA8324C

`.ASPXAUTH` is the only one needed for Login

## Login

endpoint `/security/loginajax`

payload
```
__RequestVerificationToken: -Y4YIwynPUEILnVp98ibjFqwZpXErw7hhXWEamvuEkv0e2Uh8APQi8ewR1BjZCYyEpz4afFo0QriXIUNQ1aqU2V6t8I1
type: email
email: email@gmail.com
password: Password1
```
response
```
{
  "agreements": {
        ...
  },
  "showAdultLayer": false,
  "data": {
    "logged": true,
    "active": true,
    "id": "extranet_it\\email_a45da91f401d4e3b802425f935623a34",
    "sId": "18FD15BF2BC7D344A19947002DF91B58",
    "loyaltyProviderMemberId": "email_a45da91f401d4e3b802425f935623a34",
    "status": "email",
    "name": "name",
    "surname": "surname",
    "email": "email@gmail.com",
    "preffered_cinema": 23,
    "SelectedCinemaId": "23",
        ... 
  },
  "status": true,
  "error": 0,
  "message": null,
  "code": null
}
```

## Film List Given A Cinema

endpoint `/data/filmswithshowings/{23}`

payload
```
23 
```
response
```
{
  films [
    {
      id : 8329,
      image_poster : "https://cdn1.thespacecinema.it/-/media/tsc/2023/03/john-wick-4/coverig_john_wick_4_top.jpg?h=472",
      synopsis_short : "L'assassino in nero numero uno al mondo trova una via per sconfiggere la Grand Tavola. Prima di guadagnare la libertà però, John WIck dovrà affrontare un nuovo nemico che ha alleanze in tutto il mondo e i mezzi per tramutare i vecchi amici in nuovi nemici.",
      title : "John Wick 4",
      video : "https://cdn1.thespacecinema.it/-/media/tsc/2023/03/john-wick-4/new/trailer_john-wick-4.mp4",
      virtual_reality : false,
      showings : [
          {
            date_time : "2023-03-30",
            date_day : "mercoledì",
            date_long : "mercoledì 29 marzo",
            times : [
                {
                  date : "2023-03-29T17:20:00",
                  time : "17:20",
                  screen_number : "7", // sala
                  screen_type : "2D",
                  link : "/prenotare-il-biglietto/summary/{screenId}/8329/23/14310/{sessionDate}/{sessionTime}",
                  // /prenotare-il-biglietto/summary/6 <-- screen_number /8329/23/14903/  2023-03-30 <-- date_time /18-10  <-- time :<->-
                },
            ...
            ],
          },
      ],
    },
    ...
  ],
}
```

## Cinema IDs
endpoint `embedded in homepage`
```
{
   "cinemas":{
      "whatsOnCinemas":[
         {
            "CinemaName":"Beinasco",
            "CinemaId":"28",
            "CinemaSlug":"beinasco",
            "Lat":"45.0223361",
            "Lon":"7.5899646",
            "CinemaShortName":null
         },
         {
            "CinemaName":"Belpasso",
            "CinemaId":"32",
            "CinemaSlug":"belpasso",
            "Lat":"37.5426654",
            "Lon":"14.9543871999999",
            "CinemaShortName":null
         },
         {
            "CinemaName":"Bologna",
            "CinemaId":"3",
            "CinemaSlug":"bologna",
            "Lat":"44.51123",
            "Lon":"11.370569",
            "CinemaShortName":null
         },
         ...
      ]
   }
}
```

## Seating Data
endpoint `/data/SeatingData`

important note `{"x-requested-with": "XMLHttpRequest"}` is needed for this endpoint to work

payload
```
cinemaId: 23
filmId: 8329
filmSessionId: 14992
userSessionId: e281c4f9-c8d5-448a-855f-6596274c3070
```
response
```
{
  "pricing_data" : [
      {
        "type_id": "1RidWeb",
        "type_label": "Biglietto online",
        "area_pricing": [
          {
            "area_id": "standard",
            "area_label": "Standard",
            "price": "9.2",
            "code": "0144",
            "naming_code": "A000000425",
          },
          {
            "area_id": "vip",
            "area_label": "VIP",
            "has_info": false,
            "price": "10.7",
            "code": "0145",
            "naming_code": "A000000426",
          }
          ...
        ],
        ...
      }
  ]
  "seating_data" : {
      "rows" : [
            {
                "row_label" : "A", // Fila
                "columns" : [
                    {
                       "area_id" : "standard" // "standard" or "vip" or "special" (weelchair)
                       "id" : "0000000001_001_007_000",
                       "name" : "A-1",
                       "status" : 0 // 0 available, 2 or 1 or 7 unavailable 
                    },
                    ...
                ]
            },             
      ]
  }
  "session_data" : {
       "cinema_film_id" : "HO00002018",
       "endtime_formatted" : "18:30",
       "session_id" : "14992",
  }
}
```

## CheckSelection
endpoint `/data/CheckSelection`

cookie
```
userSessionId from e281c4f9-c8d5-448a-855f-6596274c3070 to e281c4f9-c8d5-448a-855f-6596274c3070|cinemaid|filmId|filmSessionId|date_time
                                                           e281c4f9-c8d5-448a-855f-6596274c3070|23|8132|15093|2023-03-30
```

payload (query)
```
cinemaId: 23
filmId: 8329
filmSessionId: 14992
userSessionId: e281c4f9-c8d5-448a-855f-6596274c3070 
```
payload (form)
```
Tickets[0][Code]: 0144
Tickets[0][Count]: 2
SeatIds[]: 0000000001_001_004_008
SeatIds[]: 0000000001_001_004_007
```
converted to json form (SpaceDevs wtf ?!?!?!)
```
}
    "Tickets[0][Count]": len(seats),
    "Tickets[0][Code]" :"0144", # 0144 standars seats
    "SeatIds": [
                seat["id"] for seat in seats
            ],
}
```


