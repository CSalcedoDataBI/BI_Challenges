//https://www.linkedin.com/feed/update/urn:li:activity:7170991492973355008?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7170991492973355008%2C7171139106347888640%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287171139106347888640%2Curn%3Ali%3Aactivity%3A7170991492973355008%29
//Ramiro Ayala Chávez
let
  S = Excel.CurrentWorkbook(){[Name = "Table1"]}[Content],
  Fx = (A, h) =>
    let
      A = A,
      h = h,
      a = 2 * A,
      b = Number.Power(h * h + 4 * A, 1 / 2),
      c = {1 .. 500},
      d = List.Generate(
        () => [i = 0, j = 1],
        each [i] < List.Count(c),
        each if [j] = List.Count(c) then [i = [i] + 1, j = [i] + 2] else [i = [i], j = [j] + 1],
        each {c{[i]}} & {c{[j] - 1}}
      ),
      e = List.Select(d, each _{0} + _{1} = b and _{0} * _{1} = a){0}
    in
      e,
  f = Table.AddColumn(S, "Base", each Fx([Area], [Hypotenuse]){0}),
  Sol = Table.AddColumn(f, "Perpendicular", each Fx([Area], [Hypotenuse]){1})
in
  Sol