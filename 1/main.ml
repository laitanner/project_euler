(*If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000. *)

let upperbound = 999;;

let rec multiples (start : int) (accum : int) : int =
  if start > 0 then
    match (start mod 3, start mod 5) with
      | (_, 0) 
      | (0, _) -> (multiples (start - 1) accum + start)
      | _ -> (multiples (start - 1) accum)
  else
    accum;;

Printf.printf "%d\n" (multiples upperbound 0)
