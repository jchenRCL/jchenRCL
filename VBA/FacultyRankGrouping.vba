Option Explicit

Sub group()
Dim Workbook As ThisWorkbook
Dim Worksheet As Worksheets
Dim grouping As Range
Dim ranking As Range
Dim faculty As Range
Dim i As Variant

Set grouping = ThisWorkbook.Worksheets("Sheet1").Range("H2:H58")
Set ranking = ThisWorkbook.Worksheets("Sheet1").Range("F2:F58")
Set faculty = ThisWorkbook.Worksheets("Sheet1").Range("G2:G58")

For i = 2 To 58
' rank increase and faculty increase
    If ranking.Cells.Rows(i).Value > 0 And faculty.Cells.Rows(i).Value > 0 Then
        grouping.Cells.Rows(i).Value = "Rank Down Faculty Up"
    ElseIf ranking.Cells.Rows(i).Value < 0 And faculty.Cells.Rows(i).Value < 0 Then
        grouping.Cells.Rows(i).Value = "Rank Up Faculty Down"
    ElseIf ranking.Cells.Rows(i).Value < 0 And faculty.Cells.Rows(i).Value > 0 Then
        grouping.Cells.Rows(i).Value = "Rank Up Faculty Up"
    ElseIf ranking.Cells.Rows(i).Value > 0 And faculty.Cells.Rows(i).Value < 0 Then
        grouping.Cells.Rows(i).Value = "Rank Down Faculty Down"
    Else
        grouping.Cells.Rows(i).Value = "Rank No Change"
    End If
Next i

End Sub

