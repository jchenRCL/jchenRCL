Option Explicit

Sub Color()

Dim Workbook As ThisWorkbook
Dim workksheet As Worksheet
Dim i As Variant
Dim S_range, U_range As Range
Dim rw As Range

Set S_range = ThisWorkbook.Worksheets("Journals with no use").Range("F2: F403")
Set U_range = ThisWorkbook.Worksheets("Use").Range("F2: F403")


For i = 2 To 403
    If U_range.Cells.Rows(i).Interior.Color = RGB(198, 224, 180) Then
        S_range.Cells.Rows(i).Value = U_range.Cells.Rows(i).Value
    End If
Next i

End Sub
