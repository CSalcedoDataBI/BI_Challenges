//https://www.linkedin.com/feed/update/urn:li:activity:7170991492973355008?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7170991492973355008%2C7171012036280201216%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287171012036280201216%2Curn%3Ali%3Aactivity%3A7170991492973355008%29
// Solution Alejandro Simon
let
  Source = Excel.CurrentWorkbook(){[Name = "Table1"]}[Content],
  Sol = Table.Combine(
    Table.AddColumn(
      Source,
      "A",
      (w) =>
        let
          a = List.Skip(
            List.Generate(
              () => [x = w[Hypotenuse], y = 1],
              each [x] > 0,
              each [x = [x] - 1, y = Number.Sqrt(Number.Power(w[Hypotenuse], 2) - x * x)],
              each [y]
            )
          ),
          b = List.Select(a, each Int64.From(_) = _),
          c = Table.FromRows({{List.Min(b), List.Max(b)}}, {"Base", "Perpendicular"})
        in
          c
    )[A]
  )
in
  Sol