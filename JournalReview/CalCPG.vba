Option Explicit

Sub CalCPG()
Dim Workbook As ThisWorkbook
Dim Worksheet As Worksheets
Dim i As Variant
Dim c_range, u_range, cpg_range As Range

' if total usage is 0 or NA, put CPG as NA
' if total usage is not 0 nor na,
' but toal cost is na, CPG = na
' others total cost/total usage and round to 2 precision

Set c_range = ThisWorkbook.Worksheets("Simple Working Subs").Range("F2:F3534")
Set u_range = ThisWorkbook.Worksheets("Simple Working Subs").Range("G2:G3534")
Set cpg_range = ThisWorkbook.Worksheets("Simple Working Subs").Range("H2:H3534")

For i = 1 To 3535
    If IsEmpty(u_range.Cells.Rows(i).Value) Or _
        IsNull(u_range.Cells.Rows(i).Value) Or _
        u_range.Cells.Rows(i).Value = "NA" Or _
        u_range.Cells.Rows(i).Value = 0 Then
            cpg_range.Cells.Rows(i).Value = "NA"
    ElseIf IsNull(c_range.Cells.Rows(i).Value) Or _
            IsEmpty(c_range.Cells.Rows(i).Value) Then
'            c_range.Cells.Rows(i).Value = 0 Then
                cpg_range.Cells.Rows(i).Value = "NA"
    Else
        cpg_range.Cells.Rows(i).Value = Round((c_range.Cells.Rows(i).Value / u_range.Cells.Rows(i).Value), 2)
    End If
Next i
        

End Sub
