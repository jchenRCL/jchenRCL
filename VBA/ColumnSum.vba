Option Explicit

Sub fill_name()

Dim Workbook As ThisWorkbook
Dim Worksheet As Worksheets
Dim i As Variant
Dim name_range As Range
Dim citation_range As Range
Dim sum_range As Range


Set name_range = ThisWorkbook.Worksheets("UR_Peers_Test_Data").Range("A2:A21251")
Set citation_range = ThisWorkbook.Worksheets("UR_Peers_Test_Data").Range("H:H")
Set sum_range = ThisWorkbook.Worksheets("UR_Peers_Test_Data").Range("B:G")

'name_range.Cells.Value = "University of Rochester"

For i = 21252 To 22660
    citation_range.Cells.Rows(i).Value = Application.WorksheetFunction.Sum(sum_range.Cells.Rows(i).Value)
Next i

End Sub

