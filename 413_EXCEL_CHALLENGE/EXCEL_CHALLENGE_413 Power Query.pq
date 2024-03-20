let
  Source = Excel.CurrentWorkbook(){0}[Content], 
  #"Grouped Rows" = Table.Group(
    Source, 
    {"ID"}, 
    {"Num", each Text.Combine(List.Transform([Num], Text.From), "|"), type text}
  ), 
  #"Sorted Rows" = Table.Sort(#"Grouped Rows", {{"ID", Order.Ascending}}), 
  #"Split Column by Delimiter" = Table.SplitColumn(
    #"Sorted Rows", 
    "Num", 
    Splitter.SplitTextByDelimiter("|", QuoteStyle.Csv), 
    {"Num 1", "Num 2", "Num 3", "Num 4", "Num 5"}
  )
in
  #"Split Column by Delimiter"