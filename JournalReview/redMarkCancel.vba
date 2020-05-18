Option Explicit

Sub markCancel()

Dim Workbook As ThisWorkbook
Dim Worksheet As Worksheets
Dim i, j As Variant
Dim pivot_ttl_range, pivot_CPG_range, can_ttl_range As Range
Dim pivot_table_range As Range

Set pivot_ttl_range = ThisWorkbook.Worksheets("pivot").Range("A7:A1052")
Set pivot_CPG_range = ThisWorkbook.Worksheets("pivot").Range("B7:B1052")
Set pivot_table_range = ThisWorkbook.Worksheets("pivot").Range("A7:G1052")
Set can_ttl_range = ThisWorkbook.Worksheets("CanList").Range("A2:A12")


For i = 1 To 1052
For j = 1 To 12

' if title names the same then mark the records in pivot tab as red

    If pivot_ttl_range.Cells.Rows(i).Value = can_ttl_range.Cells.Rows(j).Value Then
        pivot_table_range.Cells.Rows(i).Font.ColorIndex = 3
    End If
    
' if CPG >= 35 mark BG with yellow

    If pivot_CPG_range.Cells.Rows(i).Value >= 35 Then
        pivot_CPG_range.Cells.Rows(i).Interior.Color = 65535
    End If

Next j
Next i


End Sub
