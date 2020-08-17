Option Explicit

Sub convertNA()

Dim Workbook As ThisWorkbook
Dim Worksheet As Worksheets
Dim inputrange As Range
Dim cell As Range

Set inputrange = ThisWorkbook.Worksheets("WOS_Pub_Cit_Match AVG").Range("A2:AL11897")

For Each cell In inputrange.Cells
    If IsNull(cell) Or IsEmpty(cell) Then ' if the cell is null or empty, then convert to NA
        cell = "NA"
    End If
Next cell

End Sub
