#!/usr/bin/env python3
"""To be used only with visit python interface, this is a plotting script"""

import sys
import re

def save_fig(data_fname, fig_fname, timedump):
    """Plot and save figure"""
    OpenDatabase("localhost:"+data_fname)

    DeleteAllPlots()

    ## FAR Field Lines

    AddPlot("Pseudocolor", "operators/IntegralCurve/Magnetic_Field/Magnetic Field", 1, 0)
    IntegralCurveAtts = IntegralCurveAttributes()
    IntegralCurveAtts.sourceType = IntegralCurveAtts.Circle  # SpecifiedPoint, PointList, SpecifiedLine, Circle, SpecifiedPlane, SpecifiedSphere, SpecifiedBox, Selection, FieldData
    IntegralCurveAtts.pointSource = (0, 0, 0)
    IntegralCurveAtts.lineStart = (0, 0, 0)
    IntegralCurveAtts.lineEnd = (1, 0, 0)
    IntegralCurveAtts.planeOrigin = (0, 0, -10)
    IntegralCurveAtts.planeNormal = (0, 0, 1)
    IntegralCurveAtts.planeUpAxis = (0, 1, 0)
    IntegralCurveAtts.radius = 0.15
    IntegralCurveAtts.sphereOrigin = (0, 0, 0)
    IntegralCurveAtts.boxExtents = (0, 1, 0, 1, 0, 1)
    IntegralCurveAtts.useWholeBox = 1
    IntegralCurveAtts.pointList = (0, 0, 0, 1, 0, 0, 0, 1, 0)
    IntegralCurveAtts.fieldData = ()
    IntegralCurveAtts.sampleDensity0 = 10
    IntegralCurveAtts.sampleDensity1 = 2
    IntegralCurveAtts.sampleDensity2 = 2
    IntegralCurveAtts.dataValue = IntegralCurveAtts.Solid  # Solid, SeedPointID, Speed, Vorticity, ArcLength, TimeAbsolute, TimeRelative, AverageDistanceFromSeed, CorrelationDistance, Difference, Variable
    IntegralCurveAtts.dataVariable = ""
    IntegralCurveAtts.integrationDirection = IntegralCurveAtts.Both  # Forward, Backward, Both, ForwardDirectionless, BackwardDirectionless, BothDirectionless
    IntegralCurveAtts.maxSteps = 1000
    IntegralCurveAtts.terminateByDistance = 0
    IntegralCurveAtts.termDistance = 10
    IntegralCurveAtts.terminateByTime = 0
    IntegralCurveAtts.termTime = 10
    IntegralCurveAtts.maxStepLength = 0.1
    IntegralCurveAtts.limitMaximumTimestep = 0
    IntegralCurveAtts.maxTimeStep = 0.1
    IntegralCurveAtts.relTol = 0.0001
    IntegralCurveAtts.absTolSizeType = IntegralCurveAtts.FractionOfBBox  # Absolute, FractionOfBBox
    IntegralCurveAtts.absTolAbsolute = 1e-06
    IntegralCurveAtts.absTolBBox = 1e-06
    IntegralCurveAtts.fieldType = IntegralCurveAtts.Default  # Default, FlashField, M3DC12DField, M3DC13DField, Nek5000Field, NektarPPField, NIMRODField
    IntegralCurveAtts.fieldConstant = 1
    IntegralCurveAtts.velocitySource = (0, 0, 0)
    IntegralCurveAtts.integrationType = IntegralCurveAtts.DormandPrince  # Euler, Leapfrog, DormandPrince, AdamsBashforth, RK4, M3DC12DIntegrator
    IntegralCurveAtts.parallelizationAlgorithmType = IntegralCurveAtts.VisItSelects  # LoadOnDemand, ParallelStaticDomains, MasterSlave, VisItSelects
    IntegralCurveAtts.maxProcessCount = 10
    IntegralCurveAtts.maxDomainCacheSize = 3
    IntegralCurveAtts.workGroupSize = 32
    IntegralCurveAtts.pathlines = 0
    IntegralCurveAtts.pathlinesOverrideStartingTimeFlag = 0
    IntegralCurveAtts.pathlinesOverrideStartingTime = 0
    IntegralCurveAtts.pathlinesPeriod = 0
    IntegralCurveAtts.pathlinesCMFE = IntegralCurveAtts.POS_CMFE  # CONN_CMFE, POS_CMFE
    IntegralCurveAtts.displayGeometry = IntegralCurveAtts.Lines  # Lines, Tubes, Ribbons
    IntegralCurveAtts.cleanupMethod = IntegralCurveAtts.NoCleanup  # NoCleanup, Merge, Before, After
    IntegralCurveAtts.cleanupThreshold = 1e-08
    IntegralCurveAtts.cropBeginFlag = 0
    IntegralCurveAtts.cropBegin = 0
    IntegralCurveAtts.cropEndFlag = 0
    IntegralCurveAtts.cropEnd = 0
    IntegralCurveAtts.cropValue = IntegralCurveAtts.Time  # Distance, Time, StepNumber
    IntegralCurveAtts.sampleDistance0 = 10
    IntegralCurveAtts.sampleDistance1 = 10
    IntegralCurveAtts.sampleDistance2 = 10
    IntegralCurveAtts.fillInterior = 0
    IntegralCurveAtts.randomSamples = 0
    IntegralCurveAtts.randomSeed = 0
    IntegralCurveAtts.numberOfRandomSamples = 1
    IntegralCurveAtts.issueAdvectionWarnings = 1
    IntegralCurveAtts.issueBoundaryWarnings = 1
    IntegralCurveAtts.issueTerminationWarnings = 1
    IntegralCurveAtts.issueStepsizeWarnings = 1
    IntegralCurveAtts.issueStiffnessWarnings = 1
    IntegralCurveAtts.issueCriticalPointsWarnings = 1
    IntegralCurveAtts.criticalPointThreshold = 0.001
    IntegralCurveAtts.correlationDistanceAngTol = 5
    IntegralCurveAtts.correlationDistanceMinDistAbsolute = 1
    IntegralCurveAtts.correlationDistanceMinDistBBox = 0.005
    IntegralCurveAtts.correlationDistanceMinDistType = IntegralCurveAtts.FractionOfBBox  # Absolute, FractionOfBBox
    IntegralCurveAtts.selection = ""
    SetOperatorOptions(IntegralCurveAtts, 0)
    
    PseudocolorAtts = PseudocolorAttributes()
    PseudocolorAtts.scaling = PseudocolorAtts.Linear  # Linear, Log, Skew
    PseudocolorAtts.skewFactor = 1
    PseudocolorAtts.limitsMode = PseudocolorAtts.CurrentPlot  # OriginalData, CurrentPlot
    PseudocolorAtts.minFlag = 0
    PseudocolorAtts.min = 0
    PseudocolorAtts.maxFlag = 0
    PseudocolorAtts.max = 1
    PseudocolorAtts.centering = PseudocolorAtts.Natural  # Natural, Nodal, Zonal
    PseudocolorAtts.colorTableName = "Plain Blue"
    PseudocolorAtts.invertColorTable = 1
    PseudocolorAtts.opacityType = PseudocolorAtts.FullyOpaque  # ColorTable, FullyOpaque, Constant, Ramp, VariableRange
    PseudocolorAtts.opacityVariable = ""
    PseudocolorAtts.opacity = 1
    PseudocolorAtts.opacityVarMin = 0
    PseudocolorAtts.opacityVarMax = 1
    PseudocolorAtts.opacityVarMinFlag = 0
    PseudocolorAtts.opacityVarMaxFlag = 0
    PseudocolorAtts.pointSize = 0.05
    PseudocolorAtts.pointType = PseudocolorAtts.Point  # Box, Axis, Icosahedron, Octahedron, Tetrahedron, SphereGeometry, Point, Sphere
    PseudocolorAtts.pointSizeVarEnabled = 0
    PseudocolorAtts.pointSizeVar = "default"
    PseudocolorAtts.pointSizePixels = 2
    PseudocolorAtts.lineStyle = PseudocolorAtts.SOLID  # SOLID, DASH, DOT, DOTDASH
    PseudocolorAtts.lineType = PseudocolorAtts.Tube  # Line, Tube, Ribbon
    PseudocolorAtts.lineWidth = 3
    PseudocolorAtts.tubeResolution = 10
    PseudocolorAtts.tubeRadiusSizeType = PseudocolorAtts.FractionOfBBox  # Absolute, FractionOfBBox
    PseudocolorAtts.tubeRadiusAbsolute = 0.125
    PseudocolorAtts.tubeRadiusBBox = 0.005
    PseudocolorAtts.tubeRadiusVarEnabled = 0
    PseudocolorAtts.tubeRadiusVar = ""
    PseudocolorAtts.tubeRadiusVarRatio = 10
    PseudocolorAtts.tailStyle = PseudocolorAtts.Spheres  # None, Spheres, Cones
    PseudocolorAtts.headStyle = PseudocolorAtts.Spheres  # None, Spheres, Cones
    PseudocolorAtts.endPointRadiusSizeType = PseudocolorAtts.FractionOfBBox  # Absolute, FractionOfBBox
    PseudocolorAtts.endPointRadiusAbsolute = 0.125
    PseudocolorAtts.endPointRadiusBBox = 0.01
    PseudocolorAtts.endPointResolution = 10
    PseudocolorAtts.endPointRatio = 5
    PseudocolorAtts.endPointRadiusVarEnabled = 0
    PseudocolorAtts.endPointRadiusVar = ""
    PseudocolorAtts.endPointRadiusVarRatio = 10
    PseudocolorAtts.renderSurfaces = 1
    PseudocolorAtts.renderWireframe = 0
    PseudocolorAtts.renderPoints = 0
    PseudocolorAtts.smoothingLevel = 0
    PseudocolorAtts.legendFlag = 0
    PseudocolorAtts.lightingFlag = 1
    PseudocolorAtts.wireframeColor = (0, 0, 0, 0)
    PseudocolorAtts.pointColor = (0, 0, 0, 0)
    SetPlotOptions(PseudocolorAtts)
    
    # Logging for SetAnnotationObjectOptions is not implemented yet.
    AnnotationAtts = AnnotationAttributes()
    AnnotationAtts.axes2D.visible = 1
    AnnotationAtts.axes2D.autoSetTicks = 1
    AnnotationAtts.axes2D.autoSetScaling = 1
    AnnotationAtts.axes2D.lineWidth = 1
    AnnotationAtts.axes2D.tickLocation = AnnotationAtts.axes2D.Outside  # Inside, Outside, Both
    AnnotationAtts.axes2D.tickAxes = AnnotationAtts.axes2D.BottomLeft  # Off, Bottom, Left, BottomLeft, All
    AnnotationAtts.axes2D.xAxis.title.visible = 1
    AnnotationAtts.axes2D.xAxis.title.font.font = AnnotationAtts.axes2D.xAxis.title.font.Courier  # Arial, Courier, Times
    AnnotationAtts.axes2D.xAxis.title.font.scale = 1
    AnnotationAtts.axes2D.xAxis.title.font.useForegroundColor = 1
    AnnotationAtts.axes2D.xAxis.title.font.color = (0, 0, 0, 255)
    AnnotationAtts.axes2D.xAxis.title.font.bold = 1
    AnnotationAtts.axes2D.xAxis.title.font.italic = 1
    AnnotationAtts.axes2D.xAxis.title.userTitle = 0
    AnnotationAtts.axes2D.xAxis.title.userUnits = 1
    AnnotationAtts.axes2D.xAxis.title.title = "X-Axis"
    AnnotationAtts.axes2D.xAxis.title.units = ""
    AnnotationAtts.axes2D.xAxis.label.visible = 1
    AnnotationAtts.axes2D.xAxis.label.font.font = AnnotationAtts.axes2D.xAxis.label.font.Courier  # Arial, Courier, Times
    AnnotationAtts.axes2D.xAxis.label.font.scale = 1
    AnnotationAtts.axes2D.xAxis.label.font.useForegroundColor = 1
    AnnotationAtts.axes2D.xAxis.label.font.color = (0, 0, 0, 255)
    AnnotationAtts.axes2D.xAxis.label.font.bold = 1
    AnnotationAtts.axes2D.xAxis.label.font.italic = 1
    AnnotationAtts.axes2D.xAxis.label.scaling = 0
    AnnotationAtts.axes2D.xAxis.tickMarks.visible = 1
    AnnotationAtts.axes2D.xAxis.tickMarks.majorMinimum = 0
    AnnotationAtts.axes2D.xAxis.tickMarks.majorMaximum = 1
    AnnotationAtts.axes2D.xAxis.tickMarks.minorSpacing = 0.02
    AnnotationAtts.axes2D.xAxis.tickMarks.majorSpacing = 0.2
    AnnotationAtts.axes2D.xAxis.grid = 0
    AnnotationAtts.axes2D.yAxis.title.visible = 1
    AnnotationAtts.axes2D.yAxis.title.font.font = AnnotationAtts.axes2D.yAxis.title.font.Courier  # Arial, Courier, Times
    AnnotationAtts.axes2D.yAxis.title.font.scale = 1
    AnnotationAtts.axes2D.yAxis.title.font.useForegroundColor = 1
    AnnotationAtts.axes2D.yAxis.title.font.color = (0, 0, 0, 255)
    AnnotationAtts.axes2D.yAxis.title.font.bold = 1
    AnnotationAtts.axes2D.yAxis.title.font.italic = 1
    AnnotationAtts.axes2D.yAxis.title.userTitle = 0
    AnnotationAtts.axes2D.yAxis.title.userUnits = 1
    AnnotationAtts.axes2D.yAxis.title.title = "Y-Axis"
    AnnotationAtts.axes2D.yAxis.title.units = ""
    AnnotationAtts.axes2D.yAxis.label.visible = 1
    AnnotationAtts.axes2D.yAxis.label.font.font = AnnotationAtts.axes2D.yAxis.label.font.Courier  # Arial, Courier, Times
    AnnotationAtts.axes2D.yAxis.label.font.scale = 1
    AnnotationAtts.axes2D.yAxis.label.font.useForegroundColor = 1
    AnnotationAtts.axes2D.yAxis.label.font.color = (0, 0, 0, 255)
    AnnotationAtts.axes2D.yAxis.label.font.bold = 1
    AnnotationAtts.axes2D.yAxis.label.font.italic = 1
    AnnotationAtts.axes2D.yAxis.label.scaling = 0
    AnnotationAtts.axes2D.yAxis.tickMarks.visible = 1
    AnnotationAtts.axes2D.yAxis.tickMarks.majorMinimum = 0
    AnnotationAtts.axes2D.yAxis.tickMarks.majorMaximum = 1
    AnnotationAtts.axes2D.yAxis.tickMarks.minorSpacing = 0.02
    AnnotationAtts.axes2D.yAxis.tickMarks.majorSpacing = 0.2
    AnnotationAtts.axes2D.yAxis.grid = 0
    AnnotationAtts.axes3D.visible = 0
    AnnotationAtts.axes3D.autoSetTicks = 1
    AnnotationAtts.axes3D.autoSetScaling = 1
    AnnotationAtts.axes3D.lineWidth = 0
    AnnotationAtts.axes3D.tickLocation = AnnotationAtts.axes3D.Outside  # Inside, Outside, Both
    AnnotationAtts.axes3D.axesType = AnnotationAtts.axes3D.FurthestTriad  # ClosestTriad, FurthestTriad, OutsideEdges, StaticTriad, StaticEdges
    AnnotationAtts.axes3D.triadFlag = 0
    AnnotationAtts.axes3D.bboxFlag = 0
    AnnotationAtts.axes3D.xAxis.title.visible = 1
    AnnotationAtts.axes3D.xAxis.title.font.font = AnnotationAtts.axes3D.xAxis.title.font.Arial  # Arial, Courier, Times
    AnnotationAtts.axes3D.xAxis.title.font.scale = 1
    AnnotationAtts.axes3D.xAxis.title.font.useForegroundColor = 1
    AnnotationAtts.axes3D.xAxis.title.font.color = (0, 0, 0, 255)
    AnnotationAtts.axes3D.xAxis.title.font.bold = 0
    AnnotationAtts.axes3D.xAxis.title.font.italic = 0
    AnnotationAtts.axes3D.xAxis.title.userTitle = 0
    AnnotationAtts.axes3D.xAxis.title.userUnits = 1
    AnnotationAtts.axes3D.xAxis.title.title = "X-Axis"
    AnnotationAtts.axes3D.xAxis.title.units = ""
    AnnotationAtts.axes3D.xAxis.label.visible = 1
    AnnotationAtts.axes3D.xAxis.label.font.font = AnnotationAtts.axes3D.xAxis.label.font.Arial  # Arial, Courier, Times
    AnnotationAtts.axes3D.xAxis.label.font.scale = 1
    AnnotationAtts.axes3D.xAxis.label.font.useForegroundColor = 1
    AnnotationAtts.axes3D.xAxis.label.font.color = (0, 0, 0, 255)
    AnnotationAtts.axes3D.xAxis.label.font.bold = 0
    AnnotationAtts.axes3D.xAxis.label.font.italic = 0
    AnnotationAtts.axes3D.xAxis.label.scaling = 0
    AnnotationAtts.axes3D.xAxis.tickMarks.visible = 1
    AnnotationAtts.axes3D.xAxis.tickMarks.majorMinimum = 0
    AnnotationAtts.axes3D.xAxis.tickMarks.majorMaximum = 1
    AnnotationAtts.axes3D.xAxis.tickMarks.minorSpacing = 0.02
    AnnotationAtts.axes3D.xAxis.tickMarks.majorSpacing = 0.2
    AnnotationAtts.axes3D.xAxis.grid = 0
    AnnotationAtts.axes3D.yAxis.title.visible = 1
    AnnotationAtts.axes3D.yAxis.title.font.font = AnnotationAtts.axes3D.yAxis.title.font.Arial  # Arial, Courier, Times
    AnnotationAtts.axes3D.yAxis.title.font.scale = 1
    AnnotationAtts.axes3D.yAxis.title.font.useForegroundColor = 1
    AnnotationAtts.axes3D.yAxis.title.font.color = (0, 0, 0, 255)
    AnnotationAtts.axes3D.yAxis.title.font.bold = 0
    AnnotationAtts.axes3D.yAxis.title.font.italic = 0
    AnnotationAtts.axes3D.yAxis.title.userTitle = 0
    AnnotationAtts.axes3D.yAxis.title.userUnits = 1
    AnnotationAtts.axes3D.yAxis.title.title = "Y-Axis"
    AnnotationAtts.axes3D.yAxis.title.units = ""
    AnnotationAtts.axes3D.yAxis.label.visible = 1
    AnnotationAtts.axes3D.yAxis.label.font.font = AnnotationAtts.axes3D.yAxis.label.font.Arial  # Arial, Courier, Times
    AnnotationAtts.axes3D.yAxis.label.font.scale = 1
    AnnotationAtts.axes3D.yAxis.label.font.useForegroundColor = 1
    AnnotationAtts.axes3D.yAxis.label.font.color = (0, 0, 0, 255)
    AnnotationAtts.axes3D.yAxis.label.font.bold = 0
    AnnotationAtts.axes3D.yAxis.label.font.italic = 0
    AnnotationAtts.axes3D.yAxis.label.scaling = 0
    AnnotationAtts.axes3D.yAxis.tickMarks.visible = 1
    AnnotationAtts.axes3D.yAxis.tickMarks.majorMinimum = 0
    AnnotationAtts.axes3D.yAxis.tickMarks.majorMaximum = 1
    AnnotationAtts.axes3D.yAxis.tickMarks.minorSpacing = 0.02
    AnnotationAtts.axes3D.yAxis.tickMarks.majorSpacing = 0.2
    AnnotationAtts.axes3D.yAxis.grid = 0
    AnnotationAtts.axes3D.zAxis.title.visible = 1
    AnnotationAtts.axes3D.zAxis.title.font.font = AnnotationAtts.axes3D.zAxis.title.font.Arial  # Arial, Courier, Times
    AnnotationAtts.axes3D.zAxis.title.font.scale = 1
    AnnotationAtts.axes3D.zAxis.title.font.useForegroundColor = 1
    AnnotationAtts.axes3D.zAxis.title.font.color = (0, 0, 0, 255)
    AnnotationAtts.axes3D.zAxis.title.font.bold = 0
    AnnotationAtts.axes3D.zAxis.title.font.italic = 0
    AnnotationAtts.axes3D.zAxis.title.userTitle = 0
    AnnotationAtts.axes3D.zAxis.title.userUnits = 1
    AnnotationAtts.axes3D.zAxis.title.title = "Z-Axis"
    AnnotationAtts.axes3D.zAxis.title.units = ""
    AnnotationAtts.axes3D.zAxis.label.visible = 1
    AnnotationAtts.axes3D.zAxis.label.font.font = AnnotationAtts.axes3D.zAxis.label.font.Arial  # Arial, Courier, Times
    AnnotationAtts.axes3D.zAxis.label.font.scale = 1
    AnnotationAtts.axes3D.zAxis.label.font.useForegroundColor = 1
    AnnotationAtts.axes3D.zAxis.label.font.color = (0, 0, 0, 255)
    AnnotationAtts.axes3D.zAxis.label.font.bold = 0
    AnnotationAtts.axes3D.zAxis.label.font.italic = 0
    AnnotationAtts.axes3D.zAxis.label.scaling = 0
    AnnotationAtts.axes3D.zAxis.tickMarks.visible = 1
    AnnotationAtts.axes3D.zAxis.tickMarks.majorMinimum = 0
    AnnotationAtts.axes3D.zAxis.tickMarks.majorMaximum = 1
    AnnotationAtts.axes3D.zAxis.tickMarks.minorSpacing = 0.02
    AnnotationAtts.axes3D.zAxis.tickMarks.majorSpacing = 0.2
    AnnotationAtts.axes3D.zAxis.grid = 0
    AnnotationAtts.axes3D.setBBoxLocation = 0
    AnnotationAtts.axes3D.bboxLocation = (0, 1, 0, 1, 0, 1)
    AnnotationAtts.userInfoFlag = 0
    AnnotationAtts.userInfoFont.font = AnnotationAtts.userInfoFont.Arial  # Arial, Courier, Times
    AnnotationAtts.userInfoFont.scale = 1
    AnnotationAtts.userInfoFont.useForegroundColor = 1
    AnnotationAtts.userInfoFont.color = (0, 0, 0, 255)
    AnnotationAtts.userInfoFont.bold = 0
    AnnotationAtts.userInfoFont.italic = 0
    AnnotationAtts.databaseInfoFlag = 0
    AnnotationAtts.timeInfoFlag = 1
    AnnotationAtts.databaseInfoFont.font = AnnotationAtts.databaseInfoFont.Arial  # Arial, Courier, Times
    AnnotationAtts.databaseInfoFont.scale = 1
    AnnotationAtts.databaseInfoFont.useForegroundColor = 1
    AnnotationAtts.databaseInfoFont.color = (255, 255, 255, 255)
    AnnotationAtts.databaseInfoFont.bold = 0
    AnnotationAtts.databaseInfoFont.italic = 0
    AnnotationAtts.databaseInfoExpansionMode = AnnotationAtts.SmartDirectory  # File, Directory, Full, Smart, SmartDirectory
    AnnotationAtts.databaseInfoTimeScale = 1
    AnnotationAtts.databaseInfoTimeOffset = 0
    AnnotationAtts.legendInfoFlag = 0
    AnnotationAtts.backgroundColor = (255, 255, 255, 255)
    AnnotationAtts.foregroundColor = (51, 51, 51, 255)
    AnnotationAtts.gradientBackgroundStyle = AnnotationAtts.Radial  # TopToBottom, BottomToTop, LeftToRight, RightToLeft, Radial
    AnnotationAtts.gradientColor1 = (0, 0, 255, 255)
    AnnotationAtts.gradientColor2 = (0, 0, 0, 255)
    AnnotationAtts.backgroundMode = AnnotationAtts.Solid  # Solid, Gradient, Image, ImageSphere
    AnnotationAtts.backgroundImage = ""
    AnnotationAtts.imageRepeatX = 1
    AnnotationAtts.imageRepeatY = 1
    AnnotationAtts.axesArray.visible = 1
    AnnotationAtts.axesArray.ticksVisible = 1
    AnnotationAtts.axesArray.autoSetTicks = 1
    AnnotationAtts.axesArray.autoSetScaling = 1
    AnnotationAtts.axesArray.lineWidth = 0
    AnnotationAtts.axesArray.axes.title.visible = 1
    AnnotationAtts.axesArray.axes.title.font.font = AnnotationAtts.axesArray.axes.title.font.Arial  # Arial, Courier, Times
    AnnotationAtts.axesArray.axes.title.font.scale = 1
    AnnotationAtts.axesArray.axes.title.font.useForegroundColor = 1
    AnnotationAtts.axesArray.axes.title.font.color = (0, 0, 0, 255)
    AnnotationAtts.axesArray.axes.title.font.bold = 0
    AnnotationAtts.axesArray.axes.title.font.italic = 0
    AnnotationAtts.axesArray.axes.title.userTitle = 0
    AnnotationAtts.axesArray.axes.title.userUnits = 0
    AnnotationAtts.axesArray.axes.title.title = ""
    AnnotationAtts.axesArray.axes.title.units = ""
    AnnotationAtts.axesArray.axes.label.visible = 1
    AnnotationAtts.axesArray.axes.label.font.font = AnnotationAtts.axesArray.axes.label.font.Arial  # Arial, Courier, Times
    AnnotationAtts.axesArray.axes.label.font.scale = 1
    AnnotationAtts.axesArray.axes.label.font.useForegroundColor = 1
    AnnotationAtts.axesArray.axes.label.font.color = (0, 0, 0, 255)
    AnnotationAtts.axesArray.axes.label.font.bold = 0
    AnnotationAtts.axesArray.axes.label.font.italic = 0
    AnnotationAtts.axesArray.axes.label.scaling = 0
    AnnotationAtts.axesArray.axes.tickMarks.visible = 1
    AnnotationAtts.axesArray.axes.tickMarks.majorMinimum = 0
    AnnotationAtts.axesArray.axes.tickMarks.majorMaximum = 1
    AnnotationAtts.axesArray.axes.tickMarks.minorSpacing = 0.02
    AnnotationAtts.axesArray.axes.tickMarks.majorSpacing = 0.2
    AnnotationAtts.axesArray.axes.grid = 0
    SetAnnotationAttributes(AnnotationAtts)
    
    ## NEAR Field line plot
    
    AddPlot("Pseudocolor", "operators/IntegralCurve/Magnetic_Field/Magnetic Field", 1, 0)
    
    IntegralCurveAtts = IntegralCurveAttributes()
    IntegralCurveAtts.sourceType = IntegralCurveAtts.Circle  # SpecifiedPoint, PointList, SpecifiedLine, Circle, SpecifiedPlane, SpecifiedSphere, SpecifiedBox, Selection, FieldData
    IntegralCurveAtts.pointSource = (0, 0, 0)
    IntegralCurveAtts.lineStart = (0, 0, 0)
    IntegralCurveAtts.lineEnd = (1, 0, 0)
    IntegralCurveAtts.planeOrigin = (0, 0, 10)
    IntegralCurveAtts.planeNormal = (0, 0, 1)
    IntegralCurveAtts.planeUpAxis = (0, 1, 0)
    IntegralCurveAtts.radius = 0.15
    IntegralCurveAtts.sphereOrigin = (0, 0, 0)
    IntegralCurveAtts.boxExtents = (0, 1, 0, 1, 0, 1)
    IntegralCurveAtts.useWholeBox = 1
    IntegralCurveAtts.pointList = (0, 0, 0, 1, 0, 0, 0, 1, 0)
    IntegralCurveAtts.fieldData = ()
    IntegralCurveAtts.sampleDensity0 = 10
    IntegralCurveAtts.sampleDensity1 = 2
    IntegralCurveAtts.sampleDensity2 = 2
    IntegralCurveAtts.dataValue = IntegralCurveAtts.Solid  # Solid, SeedPointID, Speed, Vorticity, ArcLength, TimeAbsolute, TimeRelative, AverageDistanceFromSeed, CorrelationDistance, Difference, Variable
    IntegralCurveAtts.dataVariable = ""
    IntegralCurveAtts.integrationDirection = IntegralCurveAtts.Both  # Forward, Backward, Both, ForwardDirectionless, BackwardDirectionless, BothDirectionless
    IntegralCurveAtts.maxSteps = 1000
    IntegralCurveAtts.terminateByDistance = 0
    IntegralCurveAtts.termDistance = 10
    IntegralCurveAtts.terminateByTime = 0
    IntegralCurveAtts.termTime = 10
    IntegralCurveAtts.maxStepLength = 0.1
    IntegralCurveAtts.limitMaximumTimestep = 0
    IntegralCurveAtts.maxTimeStep = 0.1
    IntegralCurveAtts.relTol = 0.0001
    IntegralCurveAtts.absTolSizeType = IntegralCurveAtts.FractionOfBBox  # Absolute, FractionOfBBox
    IntegralCurveAtts.absTolAbsolute = 1e-06
    IntegralCurveAtts.absTolBBox = 1e-06
    IntegralCurveAtts.fieldType = IntegralCurveAtts.Default  # Default, FlashField, M3DC12DField, M3DC13DField, Nek5000Field, NektarPPField, NIMRODField
    IntegralCurveAtts.fieldConstant = 1
    IntegralCurveAtts.velocitySource = (0, 0, 0)
    IntegralCurveAtts.integrationType = IntegralCurveAtts.DormandPrince  # Euler, Leapfrog, DormandPrince, AdamsBashforth, RK4, M3DC12DIntegrator
    IntegralCurveAtts.parallelizationAlgorithmType = IntegralCurveAtts.VisItSelects  # LoadOnDemand, ParallelStaticDomains, MasterSlave, VisItSelects
    IntegralCurveAtts.maxProcessCount = 10
    IntegralCurveAtts.maxDomainCacheSize = 3
    IntegralCurveAtts.workGroupSize = 32
    IntegralCurveAtts.pathlines = 0
    IntegralCurveAtts.pathlinesOverrideStartingTimeFlag = 0
    IntegralCurveAtts.pathlinesOverrideStartingTime = 0
    IntegralCurveAtts.pathlinesPeriod = 0
    IntegralCurveAtts.pathlinesCMFE = IntegralCurveAtts.POS_CMFE  # CONN_CMFE, POS_CMFE
    IntegralCurveAtts.displayGeometry = IntegralCurveAtts.Lines  # Lines, Tubes, Ribbons
    IntegralCurveAtts.cleanupMethod = IntegralCurveAtts.NoCleanup  # NoCleanup, Merge, Before, After
    IntegralCurveAtts.cleanupThreshold = 1e-08
    IntegralCurveAtts.cropBeginFlag = 0
    IntegralCurveAtts.cropBegin = 0
    IntegralCurveAtts.cropEndFlag = 0
    IntegralCurveAtts.cropEnd = 0
    IntegralCurveAtts.cropValue = IntegralCurveAtts.Time  # Distance, Time, StepNumber
    IntegralCurveAtts.sampleDistance0 = 10
    IntegralCurveAtts.sampleDistance1 = 10
    IntegralCurveAtts.sampleDistance2 = 10
    IntegralCurveAtts.fillInterior = 0
    IntegralCurveAtts.randomSamples = 0
    IntegralCurveAtts.randomSeed = 0
    IntegralCurveAtts.numberOfRandomSamples = 1
    IntegralCurveAtts.issueAdvectionWarnings = 1
    IntegralCurveAtts.issueBoundaryWarnings = 1
    IntegralCurveAtts.issueTerminationWarnings = 1
    IntegralCurveAtts.issueStepsizeWarnings = 1
    IntegralCurveAtts.issueStiffnessWarnings = 1
    IntegralCurveAtts.issueCriticalPointsWarnings = 1
    IntegralCurveAtts.criticalPointThreshold = 0.001
    IntegralCurveAtts.correlationDistanceAngTol = 5
    IntegralCurveAtts.correlationDistanceMinDistAbsolute = 1
    IntegralCurveAtts.correlationDistanceMinDistBBox = 0.005
    IntegralCurveAtts.correlationDistanceMinDistType = IntegralCurveAtts.FractionOfBBox  # Absolute, FractionOfBBox
    IntegralCurveAtts.selection = ""
    SetOperatorOptions(IntegralCurveAtts, 0)
    
    PseudocolorAtts = PseudocolorAttributes()
    PseudocolorAtts.scaling = PseudocolorAtts.Linear  # Linear, Log, Skew
    PseudocolorAtts.skewFactor = 1
    PseudocolorAtts.limitsMode = PseudocolorAtts.CurrentPlot  # OriginalData, CurrentPlot
    PseudocolorAtts.minFlag = 0
    PseudocolorAtts.min = 0
    PseudocolorAtts.maxFlag = 0
    PseudocolorAtts.max = 1
    PseudocolorAtts.centering = PseudocolorAtts.Natural  # Natural, Nodal, Zonal
    PseudocolorAtts.colorTableName = "Plain Yellow"
    PseudocolorAtts.invertColorTable = 1
    PseudocolorAtts.opacityType = PseudocolorAtts.FullyOpaque  # ColorTable, FullyOpaque, Constant, Ramp, VariableRange
    PseudocolorAtts.opacityVariable = ""
    PseudocolorAtts.opacity = 1
    PseudocolorAtts.opacityVarMin = 0
    PseudocolorAtts.opacityVarMax = 1
    PseudocolorAtts.opacityVarMinFlag = 0
    PseudocolorAtts.opacityVarMaxFlag = 0
    PseudocolorAtts.pointSize = 0.05
    PseudocolorAtts.pointType = PseudocolorAtts.Point  # Box, Axis, Icosahedron, Octahedron, Tetrahedron, SphereGeometry, Point, Sphere
    PseudocolorAtts.pointSizeVarEnabled = 0
    PseudocolorAtts.pointSizeVar = "default"
    PseudocolorAtts.pointSizePixels = 2
    PseudocolorAtts.lineStyle = PseudocolorAtts.SOLID  # SOLID, DASH, DOT, DOTDASH
    PseudocolorAtts.lineType = PseudocolorAtts.Tube  # Line, Tube, Ribbon
    PseudocolorAtts.lineWidth = 3
    PseudocolorAtts.tubeResolution = 10
    PseudocolorAtts.tubeRadiusSizeType = PseudocolorAtts.FractionOfBBox  # Absolute, FractionOfBBox
    PseudocolorAtts.tubeRadiusAbsolute = 0.125
    PseudocolorAtts.tubeRadiusBBox = 0.005
    PseudocolorAtts.tubeRadiusVarEnabled = 0
    PseudocolorAtts.tubeRadiusVar = ""
    PseudocolorAtts.tubeRadiusVarRatio = 10
    PseudocolorAtts.tailStyle = PseudocolorAtts.Spheres  # None, Spheres, Cones
    PseudocolorAtts.headStyle = PseudocolorAtts.Spheres  # None, Spheres, Cones
    PseudocolorAtts.endPointRadiusSizeType = PseudocolorAtts.FractionOfBBox  # Absolute, FractionOfBBox
    PseudocolorAtts.endPointRadiusAbsolute = 0.125
    PseudocolorAtts.endPointRadiusBBox = 0.01
    PseudocolorAtts.endPointResolution = 10
    PseudocolorAtts.endPointRatio = 5
    PseudocolorAtts.endPointRadiusVarEnabled = 0
    PseudocolorAtts.endPointRadiusVar = ""
    PseudocolorAtts.endPointRadiusVarRatio = 10
    PseudocolorAtts.renderSurfaces = 1
    PseudocolorAtts.renderWireframe = 0
    PseudocolorAtts.renderPoints = 0
    PseudocolorAtts.smoothingLevel = 0
    PseudocolorAtts.legendFlag = 0
    PseudocolorAtts.lightingFlag = 1
    PseudocolorAtts.wireframeColor = (0, 0, 0, 0)
    PseudocolorAtts.pointColor = (0, 0, 0, 0)
    SetPlotOptions(PseudocolorAtts)
    
    ## ISOSURFACE
    
    AddPlot("Pseudocolor", "Magnetic_Field/Magnitude Current Density", 1, 0)
    AddOperator("Isosurface", 0)
    SetActivePlots(2)
    IsosurfaceAtts = IsosurfaceAttributes()
    IsosurfaceAtts.contourNLevels = 10
    print(timedump)
    if timedump < 15:
        print("Contour to 4!")
        IsosurfaceAtts.contourValue = (4)
    elif timedump == 35:
        IsosurfaceAtts.contourValue = (1.5)
    else:
        IsosurfaceAtts.contourValue = (1)
    IsosurfaceAtts.contourPercent = ()
    IsosurfaceAtts.contourMethod = IsosurfaceAtts.Value  # Level, Value, Percent
    IsosurfaceAtts.minFlag = 0
    IsosurfaceAtts.min = 0
    IsosurfaceAtts.maxFlag = 0
    IsosurfaceAtts.max = 1
    IsosurfaceAtts.scaling = IsosurfaceAtts.Linear  # Linear, Log
    IsosurfaceAtts.variable = "default"
    SetOperatorOptions(IsosurfaceAtts, 0)
    PseudocolorAtts = PseudocolorAttributes()
    PseudocolorAtts.scaling = PseudocolorAtts.Linear  # Linear, Log, Skew
    PseudocolorAtts.skewFactor = 1
    PseudocolorAtts.limitsMode = PseudocolorAtts.CurrentPlot  # OriginalData, CurrentPlot
    PseudocolorAtts.minFlag = 0
    PseudocolorAtts.min = 0
    PseudocolorAtts.maxFlag = 0
    PseudocolorAtts.max = 1
    PseudocolorAtts.centering = PseudocolorAtts.Natural  # Natural, Nodal, Zonal
    PseudocolorAtts.colorTableName = "Plain Red"
    PseudocolorAtts.invertColorTable = 1
    PseudocolorAtts.opacityType = PseudocolorAtts.FullyOpaque  # ColorTable, FullyOpaque, Constant, Ramp, VariableRange
    PseudocolorAtts.opacityVariable = ""
    PseudocolorAtts.opacity = 1
    PseudocolorAtts.opacityVarMin = 0
    PseudocolorAtts.opacityVarMax = 1
    PseudocolorAtts.opacityVarMinFlag = 0
    PseudocolorAtts.opacityVarMaxFlag = 0
    PseudocolorAtts.pointSize = 0.05
    PseudocolorAtts.pointType = PseudocolorAtts.Point  # Box, Axis, Icosahedron, Octahedron, Tetrahedron, SphereGeometry, Point, Sphere
    PseudocolorAtts.pointSizeVarEnabled = 0
    PseudocolorAtts.pointSizeVar = "default"
    PseudocolorAtts.pointSizePixels = 2
    PseudocolorAtts.lineStyle = PseudocolorAtts.SOLID  # SOLID, DASH, DOT, DOTDASH
    PseudocolorAtts.lineType = PseudocolorAtts.Tube  # Line, Tube, Ribbon
    PseudocolorAtts.lineWidth = 3
    PseudocolorAtts.tubeResolution = 10
    PseudocolorAtts.tubeRadiusSizeType = PseudocolorAtts.FractionOfBBox  # Absolute, FractionOfBBox
    PseudocolorAtts.tubeRadiusAbsolute = 0.125
    PseudocolorAtts.tubeRadiusBBox = 0.005
    PseudocolorAtts.tubeRadiusVarEnabled = 0
    PseudocolorAtts.tubeRadiusVar = ""
    PseudocolorAtts.tubeRadiusVarRatio = 10
    PseudocolorAtts.tailStyle = PseudocolorAtts.Spheres  # None, Spheres, Cones
    PseudocolorAtts.headStyle = PseudocolorAtts.Spheres  # None, Spheres, Cones
    PseudocolorAtts.endPointRadiusSizeType = PseudocolorAtts.FractionOfBBox  # Absolute, FractionOfBBox
    PseudocolorAtts.endPointRadiusAbsolute = 0.125
    PseudocolorAtts.endPointRadiusBBox = 0.01
    PseudocolorAtts.endPointResolution = 10
    PseudocolorAtts.endPointRatio = 5
    PseudocolorAtts.endPointRadiusVarEnabled = 0
    PseudocolorAtts.endPointRadiusVar = ""
    PseudocolorAtts.endPointRadiusVarRatio = 10
    PseudocolorAtts.renderSurfaces = 1
    PseudocolorAtts.renderWireframe = 0
    PseudocolorAtts.renderPoints = 0
    PseudocolorAtts.smoothingLevel = 0
    PseudocolorAtts.legendFlag = 0
    PseudocolorAtts.lightingFlag = 1
    PseudocolorAtts.wireframeColor = (0, 0, 0, 0)
    PseudocolorAtts.pointColor = (0, 0, 0, 0)
    SetPlotOptions(PseudocolorAtts)
    
    ## FAR SLICE
    
    AddPlot("Pseudocolor", "Magnetic_Field/twist_alpha", 1, 0)
    AddOperator("Slice", 0)
    SetActivePlots(3)
    SliceAtts = SliceAttributes()
    SliceAtts.originType = SliceAtts.Intercept  # Point, Intercept, Percent, Zone, Node
    SliceAtts.originPoint = (0, 0, 0)
    SliceAtts.originIntercept = -10
    SliceAtts.originPercent = 0
    SliceAtts.originZone = 0
    SliceAtts.originNode = 0
    SliceAtts.normal = (0, 0, 1)
    SliceAtts.axisType = SliceAtts.ZAxis  # XAxis, YAxis, ZAxis, Arbitrary, ThetaPhi
    SliceAtts.upAxis = (0, 1, 0)
    SliceAtts.project2d = 0
    SliceAtts.interactive = 1
    SliceAtts.flip = 0
    SliceAtts.originZoneDomain = 0
    SliceAtts.originNodeDomain = 0
    SliceAtts.meshName = "Grid/Grid"
    SliceAtts.theta = 0
    SliceAtts.phi = 90
    SetOperatorOptions(SliceAtts, 0)
    # AddOperator("Box", 0)
    # BoxAtts = BoxAttributes()
    # BoxAtts.amount = BoxAtts.Some  # Some, All
    # BoxAtts.minx = -1.2
    # BoxAtts.maxx = 1.2
    # BoxAtts.miny = -1.2
    # BoxAtts.maxy = 1.2
    # BoxAtts.minz = -10
    # BoxAtts.maxz = 10
    # BoxAtts.inverse = 0
    # SetOperatorOptions(BoxAtts, 0)

    PseudocolorAtts = PseudocolorAttributes()
    PseudocolorAtts.colorTableName = "RdBu"
    PseudocolorAtts.minFlag = 1
    PseudocolorAtts.min = -2
    PseudocolorAtts.maxFlag = 1
    PseudocolorAtts.max = 2
    SetPlotOptions(PseudocolorAtts)
    
    ## NEAR SLICE
    
    AddPlot("Pseudocolor", "Magnetic_Field/twist_alpha", 1, 0)
    AddOperator("Slice", 0)
    SetActivePlots(4)
    SliceAtts = SliceAttributes()
    SliceAtts.originType = SliceAtts.Intercept  # Point, Intercept, Percent, Zone, Node
    SliceAtts.originPoint = (0, 0, 0)
    SliceAtts.originIntercept = 10
    SliceAtts.originPercent = 0
    SliceAtts.originZone = 0
    SliceAtts.originNode = 0
    SliceAtts.normal = (0, 0, 1)
    SliceAtts.axisType = SliceAtts.ZAxis  # XAxis, YAxis, ZAxis, Arbitrary, ThetaPhi
    SliceAtts.upAxis = (0, 1, 0)
    SliceAtts.project2d = 0
    SliceAtts.interactive = 1
    SliceAtts.flip = 0
    SliceAtts.originZoneDomain = 0
    SliceAtts.originNodeDomain = 0
    SliceAtts.meshName = "Grid/Grid"
    SliceAtts.theta = 0
    SliceAtts.phi = 90
    SetOperatorOptions(SliceAtts, 0)
    # AddOperator("Box", 0)
    # BoxAtts = BoxAttributes()
    # BoxAtts.amount = BoxAtts.Some  # Some, All
    # BoxAtts.minx = -1.2
    # BoxAtts.maxx = 1.2
    # BoxAtts.miny = -1.2
    # BoxAtts.maxy = 1.2
    # BoxAtts.minz = -10
    # BoxAtts.maxz = 10
    # BoxAtts.inverse = 0
    # SetOperatorOptions(BoxAtts, 0)

    PseudocolorAtts = PseudocolorAttributes()
    PseudocolorAtts.colorTableName = "RdBu"
    PseudocolorAtts.minFlag = 1
    PseudocolorAtts.min = -2
    PseudocolorAtts.maxFlag = 1
    PseudocolorAtts.max = 2
    SetPlotOptions(PseudocolorAtts)
    
    # Begin spontaneous state
    View3DAtts = View3DAttributes()
    View3DAtts.viewNormal = (0.499063, 0.0899918, 0.86188)
    View3DAtts.focus = (0, 0, 0)
    View3DAtts.viewUp = (-0.0363853, 0.995892, -0.0829159)
    View3DAtts.viewAngle = 30
    View3DAtts.parallelScale = 10.3923
    View3DAtts.nearPlane = -20.7846
    View3DAtts.farPlane = 20.7846
    View3DAtts.imagePan = (0.0596368, 0.041593)
    View3DAtts.imageZoom = 1.5
    View3DAtts.perspective = 1
    View3DAtts.eyeAngle = 2
    View3DAtts.centerOfRotationSet = 0
    View3DAtts.centerOfRotation = (0, 0, 0)
    View3DAtts.axis3DScaleFlag = 0
    View3DAtts.axis3DScales = (1, 1, 1)
    View3DAtts.shear = (0, 0, 1)
    View3DAtts.windowValid = 1
    SetView3D(View3DAtts)
    # End spontaneous state
    
    DrawPlots() 

    swatts = SaveWindowAttributes()
    swatts.family = 0
    swatts.format = swatts.PNG
    swatts.width = 2048
    swatts.height = 2048
    swatts.fileName = fig_fname
    swatts.SetOutputToCurrentDirectory(True)
    SetSaveWindowAttributes(swatts)

    SaveWindow()

def main():
    """Main"""
    # Get files to generate figs from
    with open("filename_list", 'r') as filep:
        filenames = filep.read().split()

    for filename in filenames:
        print("Opening " + filename)

        # scrape info from filenames
        params, visc_mode = re.search('\/(v.*)-(switching|isotropic)/', filename).groups()
        t_step = re.search('/(\d+).sdf', filename).groups()[0]

        # Form output filenames
        if visc_mode == "switching":
            fig_fname = params + "-switching_" + t_step
        else:
            fig_fname = params + "-isotropic_" + t_step

        # fig_fname = "initial_field"

        if not os.path.isfile(fig_fname+".png"):
            print("Plotting " + fig_fname)
            save_fig(filename, fig_fname, int(t_step))

    sys.exit()

main()
